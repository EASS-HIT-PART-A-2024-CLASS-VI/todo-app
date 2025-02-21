import streamlit as st
import requests

BASE_URL = "http://backend:8001/todo/"

# הצגת כותרת ראשית
st.title("To-Do List")

# פונקציה ליצירת משימה חדשה
def create_task():
    title = st.text_input("Title")
    description = st.text_area("Description")
    due_date = st.text_input("Due Date (YYYY-MM-DD HH:MM)")

    if st.button("Create Task"):
        if title and description and due_date:
            try:
                response = requests.post(BASE_URL, json={"title": title, "description": description, "due_date": due_date})
                if response.status_code == 200:
                    st.success("Task created successfully")
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to the server: {e}")
        else:
            st.warning("Please fill out all fields")

# פונקציה להציג את כל המשימות
def display_tasks():
    try:
        response = requests.get(BASE_URL)  # שליחת בקשה ל-API לקבלת כל המשימות
        if response.status_code == 200:
            tasks = response.json()

            # הצגת המשימות
            tasks.sort(key=lambda x: x['due_date'])  # מיון לפי תאריך

            for task in tasks:
                st.write(f"**{task['title']}**: {task['description']} - Due: {task['due_date']}")
                # כפתור למחיקת המשימה
                if st.button(f"Delete {task['title']}"):
                    delete_task(task['title'])
        else:
            st.error(f"Error fetching tasks: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the server: {e}")

# פונקציה למחיקת משימה
def delete_task(title):
    try:
        response = requests.delete(f"{BASE_URL}{title}")
        if response.status_code == 200:
            st.success(f"Task '{title}' deleted successfully")
        else:
            st.error(f"Error deleting task: {response.json()['detail']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the server: {e}")

# בחירה בין יצירת משימה לבין הצגת המשימות
task_option = st.selectbox("Choose an action", ["Create Task", "Display Tasks"])

# הצגת החלקים בהתאם לבחירה של המשתמש
if task_option == "Create Task":
    create_task()
elif task_option == "Display Tasks":
    display_tasks()
