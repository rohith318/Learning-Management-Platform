from pydantic import BaseModel, EmailStr
from pydantic import BaseModel
from datetime import date
from typing import List
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr



# -------------------------
# User Schemas
# -------------------------

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


# -------------------------
# Enrollment Schemas
# -------------------------

class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int


class ProgressCreate(BaseModel):
    enrollment_id: int
    completed_lessons: int
    progress_percent: float


# -------------------------
# Plan Schemas
# -------------------------

class PlanResponse(BaseModel):
    id: int
    name: str
    price: float
    duration_days: int

    class Config:
        from_attributes = True


# -------------------------
# Subscription Schemas
# -------------------------

class SubscriptionCreate(BaseModel):
    plan_id: int


class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    plan_id: int
    status: str

    class Config:
        from_attributes = True


# -------------------------
# Payment Schemas
# -------------------------

class PaymentResponse(BaseModel):
    id: int
    amount: float
    payment_date: str

    class Config:
        from_attributes = True

class AttendanceRecord(BaseModel):
    student_id: int
    status: str


class AttendanceMarkRequest(BaseModel):
    course_id: int
    date: date
    records: List[AttendanceRecord]


class AttendanceResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    date: date
    status: str

    class Config:
        from_attributes = True        

class AssignmentResponse(BaseModel):
    id: int
    course_id: int
    title: str
    description: Optional[str] = None
    deadline: datetime
    file_url: Optional[str] = None
    created_by: int

    class Config:
        from_attributes = True


class GradeSubmissionRequest(BaseModel):
    submission_id: int
    grade: str
    remarks: Optional[str] = None


class SubmissionResponse(BaseModel):
    id: int
    assignment_id: int
    student_id: int
    file_url: str
    submitted_at: datetime
    grade: Optional[str] = None
    remarks: Optional[str] = None

    class Config:
        from_attributes = True

class OtpRequest(BaseModel):
    email: str

class OtpVerifyRequest(BaseModel):
    email: EmailStr
    otp: str    

class ForgotPasswordRequest(BaseModel):
    email: EmailStr    

class VerifyForgotPasswordOtpRequest(BaseModel):
    email: EmailStr
    otp: str


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    new_password: str    