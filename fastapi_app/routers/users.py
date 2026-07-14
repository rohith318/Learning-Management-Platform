from fastapi import APIRouter, HTTPException
from accounts.models import User
from fastapi_app.schemas import UserRegister
from fastapi_app.auth import create_access_token
from fastapi_app.schemas import UserLogin
from django.contrib.auth.hashers import check_password
from fastapi import Depends
from fastapi_app.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register")
def register_user(user: UserRegister):

    if User.objects.filter(email=user.email).exists():
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    username = user.email.split("@")[0]

    new_user = User.objects.create_user(
        username=username,
        email=user.email,
        password=user.password,
        full_name=user.name,
        role=user.role,
    )

    return {
        "message": "User registered successfully",
        "id": new_user.id,
        "username": new_user.username,
        "full_name": new_user.full_name,
        "email": new_user.email,
        "role": new_user.role,
    }

@router.post("/login")
def login(user: UserLogin):

    db_user = User.objects.filter(
        email=user.email
    ).first()

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Email"
        )

    if not check_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    access_token = create_access_token(
        {
            "user_id": db_user.id,
            "email": db_user.email,
            "role": db_user.role,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "full_name": db_user.full_name,
            "email": db_user.email,
            "role": db_user.role,
        },
    }

@router.get("/me")
def get_logged_in_user(
    current_user: dict = Depends(get_current_user)
):
    return {
        "message": "JWT Authentication Successful",
        "user": current_user
    }