# todo-app
To-Do List application for task management, built with FastAPI for the backend, Redis for data storage, and Streamlit for the user interface. The app allows users to create, read, update, and delete tasks, and provides a simple, intuitive UI for managing daily tasks efficiently.
# To-Do List Application

A simple To-Do List application built using FastAPI, Redis, and Streamlit. This application allows users to manage tasks effectively with a user-friendly interface. Users can create, update, delete, and display tasks.

🚀 Features

- **Task Management**: Add, update, delete, and view tasks.
- **Backend**: FastAPI for high-performance API handling.
- **Data Storage**: Redis for fast data storage and retrieval.
- **User Interface**: Streamlit for easy-to-use, dynamic UI.
  
## 🗂️ Project Architecture

todo-app/ 
├── backend/ # FastAPI backend services │
  ├── app/ # Application files │ 
    │ ├── main.py # Main FastAPI app │
    │ └── models.py # Task models and database interactions │
 ├── Dockerfile # Backend Docker container
├── frontend/ # Streamlit frontend 
  ├── app.py # Streamlit app file │
  └── Dockerfile # Frontend Docker container 
└── docker-compose.yml # Docker Compose orchestration 
└── README.md # Project documentation

## 🛠️ Setting Up the Project

1️⃣ Clone the Repository

git clone https://github.com/your-repo-name/todo-app.git
todo-app
2️⃣ Build and Run the Containers
Ensure that you have Docker and Docker Compose installed. Run the following command to build and start the services:

docker-compose up --build

This will start the backend (FastAPI), frontend (Streamlit), and Redis services.

3️⃣ Access the Application
Frontend (Streamlit): Open your browser and go to http://localhost:8501 to interact with the To-Do List app.
Backend (FastAPI): Access the API documentation at http://localhost:8001/docs.

📚 Backend API
POST /todo/: Create a new task.
GET /todo/: Get all tasks.
GET /todo/{title}: Get task by title.
PUT /todo/{title}: Update an existing task.
DELETE /todo/{title}: Delete a task.

🖥️ Frontend
The Streamlit frontend provides an easy-to-use interface for managing tasks:
Create Task: Add new tasks with a title, description, and due date.
Display Tasks: View the list of tasks with their details.
Update and Delete: Modify or remove tasks as needed.

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
This will set up the backend, frontend, and Redis service.

Access the app in your browser:
Frontend (Streamlit): http://localhost:8501
Backend (FastAPI): http://localhost:8001/docs

🧪 Testing
The project includes basic testing for the FastAPI endpoints. To run the tests, execute the following:
cd backend
pytest

👨‍💻 Author
Name: Yotam Hasid
Email: 19yotam@gmail.com
GitHub: YotamHasid
