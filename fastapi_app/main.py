import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from fastapi import FastAPI

from fastapi_app.routers import users
from fastapi_app.routers import courses
from fastapi_app.routers import enrollments
from fastapi_app.routers import progress

app = FastAPI(
    title="Learning Management Platform API",
    description="FastAPI User Panel",
    version="1.0.0",
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(enrollments.router)
app.include_router(progress.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Learning Management Platform API"
    }