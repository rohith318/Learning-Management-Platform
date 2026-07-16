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