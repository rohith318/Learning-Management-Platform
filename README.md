# Learning Management Platform (LMS)

## Learning Management Platform (LMS) with Subscription-Based Video Learning, Analytics Dashboard, Notification System, Real-Time Collaboration, Authentication System & Advanced Backend Features

---

# Project Overview

The **Learning Management Platform (LMS)** is a full-stack web application developed using **Django** and **FastAPI**. The platform enables administrators, instructors, and students to efficiently manage online learning.

Students can register, log in using username/password, authenticate using OTP, recover forgotten passwords, sign in using Google, GitHub, or Facebook, enroll in courses, watch video lessons, purchase subscription plans, submit assignments, track attendance and learning progress, receive notifications, communicate through real-time chat, and download certificates.

Administrators can manage users, instructors, courses, lessons, enrollments, subscriptions, payments, notifications, attendance, assignments, reports, and monitor platform performance through an interactive analytics dashboard.

The project combines the following modules:

- Learning Management Platform (LMS)
- Authentication System
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
- JWT Authentication
- OAuth 2.0
- Google OAuth
- GitHub OAuth
- Facebook OAuth
- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- WebSockets
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

## 2. Authentication Module

The Authentication Module provides secure authentication using Django and FastAPI.

### Features

- User Registration
- User Login
- JWT Authentication
- Get Current User
- OTP Login
- Email OTP Verification
- Forgot Password
- Reset Password
- Google OAuth Login
- GitHub OAuth Login
- Facebook OAuth Login
- Role-Based Authentication
- Secure Password Hashing
- Django Session Integration
- Social Login Dashboard Redirect

---

## 3. Subscription-Based Video Learning Platform

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

## 4. Analytics Dashboard & Notification System

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

## 5. Real-Time Collaboration & Messaging Module

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

## 6. Advanced LMS Backend Features

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
- JWT Authentication

---

## Authentication APIs

### Username & Password Authentication

- User Registration
- User Login
- Get Current User
- JWT Authentication

### OTP Authentication

- Send OTP
- Verify OTP
- Forgot Password
- Verify Forgot Password OTP
- Reset Password

### Social Authentication

- Google OAuth Login
- GitHub OAuth Login
- Facebook OAuth Login

---

## Course APIs

- Get All Courses
- Get Course By ID
- Get Premium Courses
- Get Subscription Plans

---

## Enrollment APIs

- Enroll Student

---

## Progress APIs

- Update Progress
- Get Progress

---

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

## Authentication

| Method | Endpoint |
|----------|-------------------------------------------|
| POST | /auth/otp/send |
| POST | /auth/otp/verify |
| POST | /auth/otp/forgot-password |
| POST | /auth/otp/verify-forgot-password-otp |
| POST | /auth/otp/reset-password |
| GET | /auth/google/login |
| GET | /auth/github/login |
| GET | /auth/facebook/login |

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
│   ├── authentication/
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

- User Registration
- User Login
- OTP Login
- Forgot Password
- Reset Password
- Google Login
- GitHub Login
- Facebook Login
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
- JWT Authentication (Postman)
- Authentication API Testing
- Postman API Testing

---

# Deliverables

- Source Code
- GitHub Repository
- README Documentation
- Postman Collection
- Authentication Module
- JWT Authentication
- OTP Authentication
- Google OAuth Login
- GitHub OAuth Login
- Facebook OAuth Login
- Attendance Management Module
- Assignment Management Module
- Notification System
- Analytics Dashboard
- Reports Dashboard
- Real-Time Chat Module
- WebSocket Integration
- FastAPI APIs
- Certificate Generation
- Invoice PDF Generation

---

# Learning Outcomes

This project demonstrates practical implementation of:

- Django Web Development
- FastAPI REST APIs
- SQLAlchemy ORM
- JWT Authentication
- OAuth Authentication
- Google OAuth Integration
- GitHub OAuth Integration
- Facebook OAuth Integration
- OTP Authentication
- Email OTP Verification
- Forgot Password Workflow
- Password Reset Workflow
- Secure Authentication & Authorization
- Role-Based Access Control
- WebSocket Communication
- Real-Time Messaging
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
- Refresh Token Authentication
- Multi-Factor Authentication (MFA)
- Email Verification
- SMS OTP Authentication
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

Developed using:

- Django
- FastAPI
- JWT Authentication
- Google OAuth
- GitHub OAuth
- Facebook OAuth
- WebSockets

---

# Submission Deliverables

✔️ Learning Management Platform (LMS)

✔️ Authentication Module

✔️ User Registration

✔️ User Login

✔️ JWT Authentication

✔️ OTP Authentication

✔️ Forgot Password & Reset Password

✔️ Google OAuth Login

✔️ GitHub OAuth Login

✔️ Facebook OAuth Login

✔️ Attendance Management (FastAPI)

✔️ Assignment Management (FastAPI)

✔️ Notification System

✔️ Analytics Dashboard

✔️ Reports Dashboard

✔️ Real-Time Chat Module

✔️ WebSocket Integration

✔️ FastAPI APIs

✔️ Postman Collection

✔️ README Documentation

✔️ GitHub Repository

---

# Authentication Summary

The LMS Authentication Module supports multiple authentication methods for secure access to the platform.

### Implemented Features

- Username & Password Login
- JWT Token Authentication
- Current User API
- Email OTP Login
- Forgot Password via OTP
- Password Reset
- Google Social Login
- GitHub Social Login
- Facebook Social Login
- Django Session Integration
- Role-Based Dashboard Redirect
- Authentication API Testing using Postman

---

## Authentication API Endpoints

| Method | Endpoint |
|---------|-------------------------------------------|
| POST | /users/register |
| POST | /users/login |
| GET | /users/me |
| POST | /auth/otp/send |
| POST | /auth/otp/verify |
| POST | /auth/otp/forgot-password |
| POST | /auth/otp/verify-forgot-password-otp |
| POST | /auth/otp/reset-password |
| GET | /auth/google/login |
| GET | /auth/github/login |
| GET | /auth/facebook/login |

---

## Project Status

**Project Status:** ✅ Completed

All core LMS modules, authentication features, analytics, notifications, real-time messaging, attendance management, assignment management, and FastAPI APIs have been successfully implemented and tested.
