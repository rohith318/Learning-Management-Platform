from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int


class ProgressCreate(BaseModel):
    enrollment_id: int
    completed_lessons: int
    progress_percent: float


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True