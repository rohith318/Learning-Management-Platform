import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from fastapi import FastAPI

from fastapi_app.routers import users
from fastapi_app.routers import courses
from fastapi_app.routers import enrollments
from fastapi_app.routers import progress
from fastapi_app.routers import subscriptions
from fastapi_app.routers import payments
from fastapi_app.chat import websocket as chat_websocket
from fastapi_app.chat import api as chat_api
from fastapi_app.chat import status as chat_status
from fastapi_app.notifications import api as notification_api
from fastapi_app.notifications.service import add_notification
from fastapi_app.routers import chat_users
from fastapi.middleware.cors import CORSMiddleware
from fastapi_app.routers import attendance
from fastapi_app.database import Base, engine
import fastapi_app.models
from fastapi_app.routers import assignments
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Learning Management Platform API",
    description="FastAPI User Panel",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(enrollments.router)
app.include_router(progress.router)
app.include_router(subscriptions.router)
app.include_router(payments.router)
app.include_router(chat_websocket.router)
app.include_router(chat_api.router)
app.include_router(chat_status.router)
app.include_router(notification_api.router)
app.include_router(chat_users.router)
app.include_router(attendance.router)
app.include_router(assignments.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Learning Management Platform API"
    }