# task-manager-api
A task management REST API with authentication and CRUD functionality.

## Project Overview

A secure backend service that allows users to create accounts and manage their own tasks through an API - the engine behind what could be a full product in the future. 

### System Overview
1. A user will register, sending their name, email and password. The system will hash the password and store the user in a database. 
2. The system will verify the password, generate a JWT token and return that token (the user's proof of identify).
3. The user will create tasks with a title, description, due date and status. The system will check their token, confirm who they are and save that task with `owner_id=user.id`. 
4. The user will ask to view their and the system will check their token, query the database for tasks where `owner_id=user.id` and return only their tasks. 

## Tech Stack

* Python
* FastAPI - automatic docs
* MySQL
* SQLAlchemy (ORM)
* Pydantic (comes with FastAPI)
* JWT (python-jose)
* Passlib (password hashing)

## Features

* User registration/login
* Password hashing
* Token-based authentication
* Task CRUD
* Ownership enforcement

## How to Run Locally

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

## API Endpoints Summary