To-Do List Application

A simple To-Do List application built using FastAPI, Redis, and Streamlit. This application allows users to manage tasks effectively with a user-friendly interface. Users can create, update, delete, and display tasks.

🚀 Features
- Task Management: Add, update, delete, and view tasks.
- Backend: FastAPI for high-performance API handling.
- Data Storage: Redis for fast data storage and retrieval.
- User Interface: Streamlit for easy-to-use, dynamic UI.

🗂️ Project Architecture


![image](https://github.com/user-attachments/assets/9918b627-3b59-4195-9136-41c10fb28e88)




Arch Diagram: 

![image](https://github.com/user-attachments/assets/c17b206e-1212-4113-bccb-a1381de99e04)




🛠️ Setting Up the Project


1️⃣ Clone the Repository


git clone https://github.com/your-repo-name/todo-app.git todo-app


cd todo-app


2️⃣ Build and Run the Containers


Ensure that you have Docker and Docker Compose installed. Run the following command to build and start the services:


docker-compose up --build


3️⃣ Access the Application


Frontend (Streamlit): Open your browser and go to http://localhost:8501 to interact with the To-Do List app.


Backend (FastAPI): Access the API documentation at http://localhost:8001/docs.


📚 Backend API


![image](https://github.com/user-attachments/assets/36093588-b136-477a-bede-188a9ad7b807)


POST /todo/: Create a new task.


GET /todo/: Get all tasks.


GET /todo/{title}: Get task by title.


PUT /todo/{title}: Update an existing task.


DELETE /todo/{title}: Delete a task.


🖥️ Frontend

![image](https://github.com/user-attachments/assets/d396063d-e499-41f7-9229-3353618b74a9)



The Streamlit frontend provides an easy-to-use interface for managing tasks:


- Create Task: Add new tasks with a title, description, and due date.

  
- Display Tasks: View the list of tasks with their details.

  
- Update and Delete: Modify or remove tasks as needed.

  
🔧 Technologies Used


Backend: FastAPI, Redis


Frontend: Streamlit


Containerization: Docker, Docker Compose


📑 Installation


To run the application locally, follow these steps:


Clone the repository:


git clone https://github.com/your-repo-name/todo-app.git


cd todo-app

Build and run the application with Docker Compose:


docker-compose up --build

Access the app in your browser:


Frontend (Streamlit): http://localhost:8501


Backend (FastAPI): http://localhost:8001/docs


🧪 Testing


The project includes basic testing for the FastAPI endpoints. To run the tests, execute the following:

cd backend


pytest


![image](https://github.com/user-attachments/assets/00197ae9-afef-4d05-93a1-928d6f90ceb0)



My project video: https://youtu.be/l_GpxKbsQ78


👨‍💻 Author


Name: Yotam Hasid


Email: 19yotam@gmail.com


GitHub: YotamHasid
