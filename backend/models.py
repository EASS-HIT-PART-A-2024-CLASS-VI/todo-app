from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[str] = None

    # אין צורך להוסיף פונקציה נוספת, פשוט משתמשים ב- dict() ישירות
