# Learning Management Platform (LMS)

## Learning Management Platform (LMS) with Subscription-Based Video Learning, Analytics Dashboard, Notification System & Real-Time Collaboration Module

---

# Project Overview

The **Learning Management Platform (LMS)** is a full-stack web application developed using **Django** and **FastAPI**. The platform enables administrators, instructors, and students to manage online learning efficiently.

Students can register, enroll in courses, watch video lessons, purchase subscription plans, track their learning progress, receive notifications, communicate through real-time chat, and download certificates.

Administrators can manage users, instructors, courses, lessons, enrollments, subscriptions, payments, notifications, reports, and monitor platform performance through an interactive analytics dashboard.

The project combines four major modules:

- Learning Management Platform (LMS)
- Subscription-Based Video Learning Platform
- Analytics Dashboard & Notification System
- Real-Time Collaboration & Messaging Module

---

# Technologies Used

- Python 3
- Django
- FastAPI
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

### Chat Analytics

- Total Chat Messages
- Private Messages
- Group Messages
- Today's Messages
- Daily Chat Activity Chart

### Notification System

- In-App Notifications
- Notification Bell
- Notification Count
- Login Notifications
- Chat Notifications
- Mark Notification as Read

### Activity Logging

- User Login Activity
- Course Enrollment Activity
- Progress Update Activity
- Activity History

---

# 4. Real-Time Collaboration & Messaging Module

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

# Django Admin Features

- Admin Login
- Dashboard
- User Management
- Instructor Management
- Course Management
- Lesson Management
- Enrollment Management
- Progress Management
- Subscription Management
- Payment Management
- Chat Message Management
- Notification Management
- Activity Log Management
- Analytics Dashboard
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

## Subscription APIs

- Purchase Subscription

## Payment APIs

- Payment History

## Notification APIs

- Get Notifications
- Mark Notification as Read

## Analytics APIs

- Analytics Overview

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

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

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

## Subscription

| Method | Endpoint |
|----------|---------------------------|
| POST | /subscribe/ |

---

## Payments

| Method | Endpoint |
|----------|---------------------------|
| GET | /payments/ |

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
│── chat/
│── courses/
│── dashboard/
│── fastapi_app/
│   ├── chat/
│   ├── users/
│   ├── notifications/
│   ├── courses/
│
│── templates/
│── static/
│   ├── css/
│   ├── js/
│
│── media/
│── manage.py
│── requirements.txt
│── README.md
```

---

# Screenshots

The project includes screenshots of:

- Login Page
- Admin Dashboard
- Student Dashboard
- Analytics Dashboard
- Revenue Analytics
- Chat Analytics Dashboard
- Private Chat
- Group Chat
- Notification Bell
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
- Analytics Dashboard
- Chat Analytics Dashboard
- Real-Time Chat Module
- WebSocket Integration
- Notification System
- Activity Logging
- FastAPI APIs
- JWT Authentication
- Certificate Generation
- Invoice PDF Generation

---

# Learning Outcomes

This project demonstrates practical implementation of:

- Django Web Development
- FastAPI REST APIs
- WebSocket Communication
- Real-Time Messaging
- JWT Authentication
- Role-Based Access Control
- Analytics Dashboard Development
- Chat Analytics
- Notification Management
- Activity Logging
- Database Design
- PDF Generation
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