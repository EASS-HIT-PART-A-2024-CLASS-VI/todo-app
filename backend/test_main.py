from fastapi.testclient import TestClient
from main import app
import sys
import os

# הוספת הנתיב של הקובץ
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# יצירת מופע של ה-Client של FastAPI לצורך בדיקות
client = TestClient(app)

def test_create_task():
    response = client.post("/todo/", json={"title": "Test Task", "description": "Testing", "due_date": "2025-02-20"})
    assert response.status_code == 200
    assert response.json()["message"] == "Task 'Test Task' created successfully"  # בדיקת ההודעה

def test_get_tasks():
    response = client.get("/todo/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # בדיקה שהתשובה היא רשימה

def test_get_task_by_title():
    response = client.get("/todo/Test Task")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"  # בדיקת שם המשימה

def test_update_task():
    response = client.put("/todo/Test Task", json={"title": "Updated Task", "description": "Updated description", "due_date": "2025-02-22"})
    assert response.status_code == 200
    assert response.json()["message"] == "Task 'Test Task' updated successfully"  # בדיקת ההודעה

def test_delete_task():
    response = client.delete("/todo/Test Task")
    assert response.status_code == 200
    assert response.json()["message"] == "Task 'Test Task' deleted successfully"  # בדיקת ההודעה

def test_get_nonexistent_task():
    response = client.get("/todo/Nonexistent Task")
    assert response.status_code == 404  # בדיקת סטטוס 404 כאשר המשימה לא קיימת
