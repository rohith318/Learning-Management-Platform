# Learning Management Platform

## Project Overview

This project is a Learning Management Platform developed using Django and FastAPI.

- Django is used for the Admin Panel.
- FastAPI is used for the User Panel APIs.
- Both applications share the same database.

---

## Technologies Used

- Python
- Django
- FastAPI
- SQLite (Development)
- JWT Authentication
- Bootstrap 5
- HTML
- CSS
- JavaScript
- ReportLab

---

## Features

### Django Admin Panel

- Admin Login
- Dashboard
- User Management
- Course Management
- Lesson Management
- Enrollment Management
- Progress Management
- Reports Dashboard
- PDF Report Generation

### FastAPI User Panel

- User Registration API
- User Login API
- JWT Authentication
- Protected API (/users/me)
- Courses API
- Enrollment API
- Progress API

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

### Install Packages

```bash
pip install -r requirements.txt
```

### Run Django

```bash
python manage.py runserver
```

### Run FastAPI

```bash
uvicorn fastapi_app.main:app --reload --port 8001
```

---

## API Documentation

```
http://127.0.0.1:8001/docs
```

---

## Admin Panel

```
http://127.0.0.1:8000/login/
```

---

## Developed By

Rohith Raj