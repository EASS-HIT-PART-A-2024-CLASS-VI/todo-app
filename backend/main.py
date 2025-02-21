from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn
import redis
from models import Todo
from database import redis_con

app = FastAPI(title="To-do List API")

# חיבור ל-Redis עם הכתובת "redis" בקונטיינר של Docker
redis_con = redis.StrictRedis(host="redis", port=6379, db=0, decode_responses=True)

# יצירת משימה חדשה
@app.post('/todo/')
def create_todo(todo: Todo):
    if redis_con.exists(todo.title):
        raise HTTPException(status_code=400, detail="Task already exists")
    redis_con.hset(todo.title, mapping=todo.dict(exclude_unset=True))

    return {"message": "Task created successfully", "task": todo}

# שליפת כל המשימות
@app.get('/todo/', response_model=List[Todo])
def get_all_todos():
    tasks = []
    for key in redis_con.keys():
        task_data = redis_con.hgetall(key)
        
        # שינוי בקוד: המרה רק אם הנתונים הם bytes
        task_data = {k.decode('utf-8') if isinstance(k, bytes) else k: v.decode('utf-8') if isinstance(v, bytes) else v for k, v in task_data.items()}
        
        tasks.append(Todo(**task_data))
    return tasks

# שליפת משימה לפי כותרת
@app.get('/todo/{title}')
def get_todo(title: str):
    task = redis_con.hgetall(title)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # שינוי בקוד: המרה רק אם הנתונים הם bytes
    task = {k.decode('utf-8') if isinstance(k, bytes) else k: v.decode('utf-8') if isinstance(v, bytes) else v for k, v in task.items()}
    
    return Todo(**task)

# עדכון משימה
@app.put('/todo/{title}')
def update_todo(title: str, todo: Todo):
    if not redis_con.exists(title):
        raise HTTPException(status_code=404, detail="Task not found")
    redis_con.hset(title, mapping=todo.model_dump())
    return {"message": "Task updated successfully", "task": todo}

# מחיקת משימה
@app.delete('/todo/{title}')
def delete_todo(title: str):
    if not redis_con.exists(title):
        raise HTTPException(status_code=404, detail="Task not found")
    redis_con.delete(title)
    return {"message": "Task deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
