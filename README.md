# Learning Management Platform (LMS)

## Learning Management Platform (LMS) with Subscription-Based Video Learning, Analytics Dashboard, Notification System, Real-Time Collaboration & Advanced Backend Features

---

# Project Overview

The **Learning Management Platform (LMS)** is a full-stack web application developed using **Django** and **FastAPI**. The platform enables administrators, instructors, and students to efficiently manage online learning.

Students can register, enroll in courses, watch video lessons, purchase subscription plans, submit assignments, track attendance and learning progress, receive notifications, communicate through real-time chat, and download certificates.

Administrators can manage users, instructors, courses, lessons, enrollments, subscriptions, payments, notifications, attendance, assignments, reports, and monitor platform performance through an interactive analytics dashboard.

The project combines the following modules:

- Learning Management Platform (LMS)
- Subscription-Based Video Learning Platform
- Analytics Dashboard & Notification System
- Real-Time Collaboration & Messaging Module
- Advanced LMS Backend Features

---

# Technologies Used

- Python 3
- Django
- FastAPI
- SQLAlchemy
- SQLite
- WebSockets
- JWT Authentication
- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- Chart.js
- ReportLab
- Uvicorn

---

# Project Modules

## 1. Learning Management Platform (LMS)

### Features

- User Registration
- User Login
- Role-Based Authentication
- Admin Dashboard
- Instructor Dashboard
- Student Dashboard
- User Profile Management
- Course Management
- Lesson Management
- Enrollment Management
- Progress Tracking
- Search Courses
- My Courses
- Video Learning
- Lesson Completion Tracking
- Next Lesson Navigation

---

## 2. Subscription-Based Video Learning Platform

Students can purchase subscription plans to access premium learning content.

### Features

- Subscription Plans
- Premium Courses
- Purchase Subscription
- Payment Management
- Payment History
- Invoice PDF Generation
- Certificate Generation
- Download Certificate
- Download Invoice

---

## 3. Analytics Dashboard & Notification System

The Analytics Dashboard provides complete insights into LMS activities.

### Dashboard Analytics

- Total Users
- Total Students
- Total Instructors
- Total Courses
- Total Lessons
- Total Enrollments
- Progress Statistics
- Monthly Revenue
- Revenue Analytics Chart
- Popular Courses
- Recent Courses
- Recent Activity

### Notification System

- In-App Notifications
- Notification Bell
- Notification Count
- Login Notifications
- Attendance Notifications
- Assignment Notifications
- Chat Notifications
- Grade Notifications
- Mark Notification as Read

### Activity Logging

- User Login Activity
- Course Enrollment Activity
- Progress Update Activity
- Attendance Activity
- Assignment Activity
- Activity History

---

## 4. Real-Time Collaboration & Messaging Module

The Real-Time Collaboration & Messaging Module enables instant communication between administrators, instructors, and students using FastAPI WebSockets.

### Features

- Real-Time Private Chat
- Real-Time Group Chat
- FastAPI WebSocket Integration
- Chat History
- Online / Offline User Status
- Live User List
- Instant Notifications
- Notification Bell Integration
- Chat Analytics Dashboard
- Django Admin Chat Management

---

## 5. Advanced LMS Backend Features

### Attendance Management (FastAPI)

#### Features

- Mark Attendance
- Student Attendance Report
- Course Attendance Report
- Attendance Percentage Calculation
- Attendance Notifications

### Assignment Management (FastAPI)

#### Features

- Create Assignment
- Upload Assignment File
- Submit Assignment
- Grade Assignment
- View Assignments
- View Submissions
- Assignment Notifications

### Reports Dashboard

- Total Students
- Total Instructors
- Total Courses
- Active Courses
- Inactive Courses
- Total Enrollments

---

# Django Admin Features

- Admin Login
- Dashboard
- User Management
- Instructor Management
- Student Management
- Course Management
- Lesson Management
- Enrollment Management
- Attendance Management
- Assignment Management
- Progress Management
- Subscription Management
- Payment Management
- Chat Message Management
- Notification Management
- Activity Log Management
- Analytics Dashboard
- Reports Dashboard
- Certificate Generation
- Invoice Generation

---

# FastAPI APIs

## User APIs

- Register User
- Login User
- Get Current User

## Course APIs

- Get All Courses
- Get Course By ID
- Get Premium Courses
- Get Subscription Plans

## Enrollment APIs

- Enroll Student

## Progress APIs

- Update Progress
- Get Progress

## Attendance APIs

| Method | Endpoint |
|----------|-------------------------------|
| POST | /attendance/mark |
| GET | /attendance/student/{student_id} |
| GET | /attendance/course/{course_id} |

### Attendance Features

- Mark Student Attendance
- Student Attendance Report
- Course Attendance Report
- Attendance Percentage Calculation
- Attendance Notifications

---

## Assignment APIs

| Method | Endpoint |
|----------|--------------------------------|
| POST | /assignments/create |
| POST | /assignments/submit |
| PUT | /assignments/grade |
| GET | /assignments/ |
| GET | /assignments/submissions |

### Assignment Features

- Create Assignment
- Upload Assignment File
- Submit Assignment
- Grade Assignment
- View Assignments
- View Submissions
- Assignment Notifications

---

## Notification APIs

- Get Notifications
- Mark Notification as Read
- Attendance Notifications
- Assignment Notifications
- Grade Notifications

---

## Analytics APIs

- Analytics Overview
- Reports Dashboard
- Student Analytics
- Course Analytics

---

## Chat APIs

- Get Chat Users
- Get Chat History
- WebSocket Chat Connection

---

# Installation Guide

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

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Django Server

Apply Migrations

```bash
python manage.py migrate
```

Run Django Server

```bash
python manage.py runserver
```

Django URL

```
http://127.0.0.1:8000/
```

---

# Run FastAPI Server

```bash
uvicorn fastapi_app.main:app --reload --port 8001
```

FastAPI URL

```
http://127.0.0.1:8001/
```

Swagger Documentation

```
http://127.0.0.1:8001/docs
```

---

# API Endpoints

## Users

| Method | Endpoint |
|----------|---------------------------|
| POST | /users/register |
| POST | /users/login |
| GET | /users/me |

---

## Courses

| Method | Endpoint |
|----------|---------------------------|
| GET | /courses/ |
| GET | /courses/{course_id} |
| GET | /courses/plans/ |
| GET | /courses/premium/ |

---

## Enrollment

| Method | Endpoint |
|----------|---------------------------|
| POST | /enrollments/ |

---

## Progress

| Method | Endpoint |
|----------|---------------------------|
| POST | /progress/ |
| GET | /progress/{user_id} |

---

## Attendance

| Method | Endpoint |
|----------|-------------------------------|
| POST | /attendance/mark |
| GET | /attendance/student/{student_id} |
| GET | /attendance/course/{course_id} |

---

## Assignments

| Method | Endpoint |
|----------|--------------------------------|
| POST | /assignments/create |
| POST | /assignments/submit |
| PUT | /assignments/grade |
| GET | /assignments/ |
| GET | /assignments/submissions |

---

## Notifications

| Method | Endpoint |
|----------|------------------------------------------|
| GET | /notifications/ |
| POST | /notifications/read/{notification_id}/ |

---

## Analytics

| Method | Endpoint |
|----------|-----------------------------|
| GET | /analytics/overview/ |
| GET | /reports/ |

---

## Chat APIs

| Method | Endpoint |
|----------|-------------------------------------------|
| GET | /chat/users |
| GET | /chat/history/{sender_id}/{receiver_id} |
| WebSocket | /ws/chat/{user_id} |

---

# Project Structure

```
Learning_Management_Platform/

│── accounts/
│── analytics_app/
│── chat/
│── courses/
│── dashboard/
│── fastapi_app/
│   ├── attendance/
│   ├── assignments/
│   ├── chat/
│   ├── courses/
│   ├── notifications/
│   ├── users/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── main.py
│
│── templates/
│── static/
│   ├── css/
│   ├── js/
│
│── media/
│── uploads/
│── manage.py
│── requirements.txt
│── README.md
```

---

# Screenshots

The project includes screenshots of:

- Login Page
- Admin Dashboard
- Instructor Dashboard
- Student Dashboard
- Analytics Dashboard
- Reports Dashboard
- Attendance Module
- Assignment Module
- Notification Bell
- Chat Dashboard
- Private Chat
- Group Chat
- Course Management
- Subscription Page
- Payment History
- Django Admin
- Postman API Testing

---

# Deliverables

- Source Code
- GitHub Repository
- README Documentation
- Postman Collection
- Attendance Management Module
- Assignment Management Module
- Notification System
- Analytics Dashboard
- Reports Dashboard
- Real-Time Chat Module
- WebSocket Integration
- FastAPI APIs
- JWT Authentication
- Certificate Generation
- Invoice PDF Generation

---

# Learning Outcomes

This project demonstrates practical implementation of:

- Django Web Development
- FastAPI REST APIs
- SQLAlchemy ORM
- WebSocket Communication
- Real-Time Messaging
- JWT Authentication
- Role-Based Access Control
- Attendance Management
- Assignment Management
- File Upload using FastAPI
- Notification Management
- Analytics Dashboard Development
- Reports Dashboard
- Database Design
- API Testing using Postman
- Git & GitHub Version Control

---

# Future Enhancements

- Stripe Payment Gateway
- Razorpay Integration
- Redis
- Celery Background Tasks
- Typing Indicator
- Read Receipts
- File Sharing
- Voice Messages
- Video Calling
- Push Notifications
- Quiz & Assessment
- Live Classes
- Discussion Forum
- Cloud Video Storage

---

# Developed By

**Rohith Raj**

### Learning Management Platform (LMS)

Developed using **Django + FastAPI + WebSockets**

---

## Submission Deliverables

✔️ Attendance Management (FastAPI)

✔️ Assignment Management (FastAPI)

✔️ Notification System

✔️ Django Analytics Dashboard

✔️ Reports Dashboard

✔️ Real-Time Chat Module

✔️ Postman Collection

✔️ README Documentation

✔️ GitHub Repository

✔️ JWT Authentication

✔️ Role-Based Access Control

✔️ WebSocket Integration

✔️ LMS Backend Features Completed