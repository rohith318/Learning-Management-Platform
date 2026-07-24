from fastapi import APIRouter
import random
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi_app.database import get_db
from fastapi_app.models import User, OTPLog
from fastapi_app.schemas import OtpRequest
from datetime import datetime
from fastapi_app.schemas import OtpVerifyRequest
from fastapi_app.auth import create_access_token
from django.core.mail import send_mail
from django.conf import settings
from fastapi_app.schemas import ForgotPasswordRequest

from django.contrib.auth.hashers import make_password
from fastapi_app.schemas import (
    VerifyForgotPasswordOtpRequest,
    ResetPasswordRequest,
)

router = APIRouter(
    prefix="/auth/otp",
    tags=["OTP Authentication"],
)


@router.post("/send")
def send_otp(
    data: OtpRequest,
    db: Session = Depends(get_db),
):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if not user:
        return {
            "message": "User not found"
        }

    otp = str(random.randint(100000, 999999))

    otp_log = OTPLog(
        user_id=user.id,
        email=user.email,
        otp=otp,
        is_verified=False,
        created_at=datetime.utcnow(),
        expires_at=datetime.utcnow() + timedelta(minutes=5),
    )

    db.add(otp_log)
    db.commit()
    db.refresh(otp_log)

    send_mail(
    subject="Your LMS OTP Code",
    message=f"""
Hello {user.username},

Your OTP is: {otp}

This OTP is valid for 5 minutes.

Do not share this OTP with anyone.

Regards,
Learning Management System
""",
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[user.email],
    fail_silently=False,
)

    return {
    "message": "OTP sent successfully",
    "email": user.email,
}

@router.post("/verify")
def verify_otp(
    data: OtpVerifyRequest,
    db: Session = Depends(get_db),
):

    otp_record = db.query(OTPLog).filter(
        OTPLog.email == data.email,
        OTPLog.otp == data.otp,
        OTPLog.is_verified == False,
    ).first()

    if not otp_record:
        return {
            "message": "Invalid OTP"
        }

    if otp_record.expires_at < datetime.utcnow():
        return {
            "message": "OTP Expired"
        }

    otp_record.is_verified = True

    db.commit()

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    access_token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id,
        }
    )

    return {
        "message": "OTP verified successfully",
        "access_token": access_token,
        "token_type": "bearer",
    }

@router.post("/forgot-password")
def forgot_password(
    data: ForgotPasswordRequest,
    db: Session = Depends(get_db),
):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if not user:
        return {
            "message": "User not found"
        }

    otp = str(random.randint(100000,999999))

    otp_log = OTPLog(
        user_id=user.id,
        email=user.email,
        otp=otp,
        is_verified=False,
        created_at=datetime.utcnow(),
        expires_at=datetime.utcnow()+timedelta(minutes=5),
    )

    db.add(otp_log)
    db.commit()

    send_mail(
        subject="Password Reset OTP",
        message=f"""
Hello {user.username},

Your password reset OTP is:

{otp}

Valid for 5 minutes.

Regards,
Learning Management System
""",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )

    return {
        "message":"Password reset OTP sent successfully"
    }

@router.post("/verify-forgot-password-otp")
def verify_forgot_password_otp(
    data: VerifyForgotPasswordOtpRequest,
    db: Session = Depends(get_db),
):

    otp_record = db.query(OTPLog).filter(
        OTPLog.email == data.email,
        OTPLog.otp == data.otp,
        OTPLog.is_verified == False,
    ).first()

    if not otp_record:
        return {
            "message": "Invalid OTP"
        }

    if otp_record.expires_at < datetime.utcnow():
        return {
            "message": "OTP Expired"
        }

    otp_record.is_verified = True

    db.commit()

    return {
        "message": "OTP verified successfully"
    }


@router.post("/reset-password")
def reset_password(
    data: ResetPasswordRequest,
    db: Session = Depends(get_db),
):

    otp_record = db.query(OTPLog).filter(
        OTPLog.email == data.email,
        OTPLog.is_verified == True,
    ).order_by(
        OTPLog.id.desc()
    ).first()

    if not otp_record:
        return {
            "message": "Please verify OTP first"
        }

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if not user:
        return {
            "message": "User not found"
        }

    user.password = make_password(data.new_password)

    db.commit()

    return {
        "message": "Password changed successfully"
    }