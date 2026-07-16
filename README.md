# Subscription-Based Video Learning Platform

## Project Overview

This project is a Subscription-Based Video Learning Platform developed using **Django** and **FastAPI**.

- Django is used for the Admin Panel.
- FastAPI is used for the User APIs.
- Both applications share the same SQLite database.
- JWT Authentication is used for secure API access.

---

# Technologies Used

- Python 3
- Django
- FastAPI
- SQLite
- JWT Authentication
- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- ReportLab
- Uvicorn

---

# Features

## Django Admin Panel

- Admin Login
- Dashboard
- User Management
- Course Management
- Lesson Management
- Subscription Plan Management
- Enrollment Management
- Progress Management
- Payment Management
- Certificate Generation
- Invoice PDF Generation

---

## FastAPI APIs

### User APIs

- Register User
- Login User
- Get Current User

### Course APIs

- Get All Courses
- Get Course By ID
- Get Subscription Plans
- Get Premium Courses

### Enrollment APIs

- Enroll Student

### Progress APIs

- Update Course Progress
- Get User Progress

### Subscription APIs

- Purchase Subscription

### Payment APIs

- Payment History

---

# User Panel Features

- User Registration
- User Login
- Student Dashboard
- My Courses
- Course Details
- Embedded YouTube Video Learning
- Mark Lesson as Completed
- Next Lesson Navigation
- Course Progress Tracking
- Buy Subscription
- Payment Success Page
- Payment History
- Download Certificate
- Download Invoice
- User Profile

---

# Installation

## Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

```bash
cd Learning_Management_Platform
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Django

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

Django URL

```
http://127.0.0.1:8000
```

---

## Run FastAPI

```bash
uvicorn fastapi_app.main:app --reload --port 8001
```

FastAPI URL

```
http://127.0.0.1:8001
```

Swagger Documentation

```
http://127.0.0.1:8001/docs
```

---

# FastAPI Endpoints

## Users

POST /users/register

POST /users/login

GET /users/me

---

## Courses

GET /courses/

GET /courses/{course_id}

GET /courses/plans/

GET /courses/premium/

---

## Enrollment

POST /enrollment/

---

## Progress

POST /progress/

GET /progress/{user_id}

---

## Subscription

POST /subscribe/

---

## Payments

GET /payments/

---

# Project Structure

```
Learning_Management_Platform/

│── accounts/

│── courses/

│── dashboard/

│── fastapi_app/

│── templates/

│── static/

│── manage.py

│── requirements.txt

│── README.md
```

---

# Project Deliverables

- Source Code
- GitHub Repository
- README Documentation
- Postman Collection
- Django Admin Panel
- FastAPI APIs
- JWT Authentication
- Certificate Generation
- Invoice PDF Generation

---

# Future Enhancements

- Stripe Payment Gateway
- Razorpay Integration
- Email Notifications
- Live Classes
- Quiz & Assessment Module
- Discussion Forum
- Video Upload to Cloud Storage

---

# Developed By

**Rohith Raj**

Subscription-Based Video Learning Platform

Developed using Django + FastAPI