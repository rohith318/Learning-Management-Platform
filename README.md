# Learning Management Platform (LMS) with Subscription-Based Video Learning, Analytics Dashboard & Notification System

## Project Overview

The **Learning Management Platform (LMS)** is a full-stack web application developed using **Django** and **FastAPI**. The platform allows students to enroll in courses, watch learning videos, purchase subscription plans, track learning progress, manage payments, and download certificates.

In addition to the core LMS features, the platform includes an **Analytics Dashboard**, **Activity Logging**, and **Notification System** for monitoring platform performance and improving user engagement.

This project combines three major modules:

- Learning Management Platform (LMS)
- Subscription-Based Video Learning Platform
- Analytics Dashboard & Notification System

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
- Chart.js
- ReportLab
- Uvicorn

---

# Project Modules

## 1. Learning Management Platform (LMS)

The LMS module allows administrators and students to manage online learning.

### Features

- User Registration
- User Login
- Role-Based Authentication
- Student Dashboard
- Instructor Dashboard
- Course Management
- Lesson Management
- Enrollment Management
- Progress Tracking
- Search Courses
- My Courses
- Video Learning
- Mark Lesson Completed
- Next Lesson Navigation
- User Profile

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

This module provides analytics, activity tracking, and notifications.

### Analytics Dashboard

- Total Users
- Total Students
- Total Instructors
- Total Courses
- Total Lessons
- Total Enrollments
- Monthly Revenue
- Popular Courses
- Dashboard Statistics Cards
- Revenue Analytics
- Course Analytics

### Notification System

- In-App Notifications
- Email Notifications
- Login Notifications
- Notification Center
- Mark Notification as Read

### Activity Logging

- User Login Activity
- Course Enrollment Activity
- Progress Update Activity
- Activity History

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
- Analytics Dashboard
- Notification Management
- Activity Log Management
- Certificate Generation
- Invoice Generation

---

# FastAPI User APIs

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

## Analytics APIs

- Analytics Overview

## Notification APIs

- Get Notifications
- Mark Notification as Read

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

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Django

Apply migrations

```bash
python manage.py migrate
```

Run server

```bash
python manage.py runserver
```

Django URL

```
http://127.0.0.1:8000/
```

---

# Run FastAPI

```bash
uvicorn fastapi_app.main:app --reload --port 8001
```

FastAPI URL

```
http://127.0.0.1:8001/
```

Swagger API

```
http://127.0.0.1:8001/docs
```

---

# API Endpoints

## Users

| Method | Endpoint |
|---------|----------|
| POST | /users/register |
| POST | /users/login |
| GET | /users/me |

---

## Courses

| Method | Endpoint |
|---------|----------|
| GET | /courses/ |
| GET | /courses/{course_id} |
| GET | /courses/plans/ |
| GET | /courses/premium/ |

---

## Enrollment

| Method | Endpoint |
|---------|----------|
| POST | /enrollments/ |

---

## Progress

| Method | Endpoint |
|---------|----------|
| POST | /progress/ |
| GET | /progress/{user_id} |

---

## Subscription

| Method | Endpoint |
|---------|----------|
| POST | /subscribe/ |

---

## Payments

| Method | Endpoint |
|---------|----------|
| GET | /payments/ |

---

## Notifications

| Method | Endpoint |
|---------|----------|
| GET | /notifications/ |
| POST | /notifications/read/{notification_id}/ |

---

## Analytics

| Method | Endpoint |
|---------|----------|
| GET | /analytics/overview/ |

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
│── media/
│── manage.py
│── requirements.txt
│── README.md
```

---

# Screenshots

The project includes screenshots of:

- Login Page
- Django Admin Dashboard
- Analytics Dashboard
- User Dashboard
- Notification Center
- Course Management
- Payment History
- Subscription Page
- Postman API Testing

---

# Deliverables

- Source Code
- GitHub Repository
- README Documentation
- Postman Collection
- Analytics Dashboard
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
- JWT Authentication
- Role-Based Access Control
- Analytics Dashboard Development
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
- Real-Time Notifications
- Email Scheduling
- Quiz & Assessment
- Live Classes
- Discussion Forum
- Cloud Video Storage

---

# Developed By

**Rohith Raj**

**Learning Management Platform (LMS) with Subscription-Based Video Learning, Analytics Dashboard & Notification System**

Developed using **Django + FastAPI**