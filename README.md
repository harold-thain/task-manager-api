# Task Management API

A REST API for managing personal tasks, built with FastAPI, SQLAlchemy, and JWT authentication.

## Project Overview

A secure backend service that allows users to create accounts and manage their own tasks through an API - the engine behind what could be a full product in the future. 

### System Overview
1. A user will register, sending their name, email and password. The system will hash the password and store the user in a database. 
2. The system will verify the password, generate a JWT token and return that token (the user's proof of identify).
3. The user will create tasks with a title, description, due date and status. The system will check their token, confirm who they are and save that task with `owner_id=user.id`. 
4. The user will ask to view their tasks and the system will check their token, query the database for tasks where `owner_id=user.id` and return only their tasks. 

## Tech Stack

- **Python 3.10+**
- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **SQLite** — database (easily swappable for MySQL)
- **PassLib + bcrypt** — password hashing
- **python-jose** — JWT tokens

## Project Structure

```
task-api/
├── app/
│   ├── main.py        # App entry point
│   ├── database.py    # DB connection and session
│   ├── models.py      # SQLAlchemy models
│   ├── schemas.py     # Pydantic schemas
│   ├── auth.py        # Auth logic (hashing, JWT)
│   └── routers/
│       ├── tasks.py   # Task CRUD routes
│       └── users.py   # Register and login routes
├── .env               # Environment variables (not committed)
├── .env.example       # Example env file (committed)
└── requirements.txt
```

## Setup

1. **Clone the repo and enter the directory**
```bash
git clone 
cd task-api
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  
# Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and set a strong SECRET_KEY
```

5. **Run the server**
```bash
uvicorn app.main:app --reload
```

6. **View the interactive API docs**

Open http://127.0.0.1:8000/docs

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users/register` | Register a new user |
| POST | `/users/login` | Login and receive JWT token |

### Tasks (all require authentication)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks` | Create a task |
| GET | `/tasks` | Get all your tasks |
| GET | `/tasks/{id}` | Get a single task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

### Query Parameters
- `GET /tasks?skip=0&limit=10` — pagination support

## Authentication

Register, then login to receive a token. Include it in subsequent requests:
```
Authorization: Bearer <your-token>
```

In the `/docs` UI, click **Authorize** and paste your token.