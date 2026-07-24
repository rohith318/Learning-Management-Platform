from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    DateTime,
    ForeignKey,
)

from fastapi_app.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy import Text, DateTime
from datetime import datetime
from sqlalchemy import Boolean
from datetime import datetime

print("Loading models.py - Start")
print("User model loaded")
print("Attendance model loaded")
print("End of models.py")

class User(Base):
    __tablename__ = "accounts_user"

    id = Column(Integer, primary_key=True, index=True)

    password = Column(String(128))

    last_login = Column(DateTime, nullable=True)

    is_superuser = Column(Boolean, default=False)

    username = Column(String(150), unique=True, index=True)

    first_name = Column(String(150), default="")

    last_name = Column(String(150), default="")

    email = Column(String(254), unique=True, index=True)

    is_staff = Column(Boolean, default=False)

    is_active = Column(Boolean, default=True)

    date_joined = Column(DateTime, default=datetime.utcnow)

    full_name = Column(String(100))

    role = Column(String(20))

class Plan(Base):
    __tablename__ = "courses_plan"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    price = Column(Float)
    duration_days = Column(Integer)


class Subscription(Base):
    __tablename__ = "courses_subscription"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("accounts_user.id"))
    plan_id = Column(Integer, ForeignKey("courses_plan.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String(20))


class Payment(Base):
    __tablename__ = "courses_payment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("accounts_user.id"))
    plan_id = Column(Integer, ForeignKey("courses_plan.id"))
    amount = Column(Float)
    payment_date = Column(DateTime)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("accounts_user.id"),
        nullable=False
    )

    course_id = Column(
        Integer,
        nullable=False
    )

    date = Column(Date, nullable=False)

    status = Column(String(20), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "course_id",
            "date",
            name="unique_attendance"
        ),
    )

    student = relationship("User")



class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    deadline = Column(DateTime, nullable=False)
    file_url = Column(String(255), nullable=True)
    created_by = Column(Integer, ForeignKey("accounts_user.id"), nullable=False)


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("accounts_user.id"), nullable=False)
    file_url = Column(String(255), nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    grade = Column(String(20), nullable=True)
    remarks = Column(String(500), nullable=True)    


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("accounts_user.id"),
        nullable=False
    )

    message = Column(String(255), nullable=False)

    link = Column(String(255), nullable=True)

    is_read = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)    

class SocialAccount(Base):
    __tablename__ = "accounts_socialaccount"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("accounts_user.id"),
        nullable=False
    )

    provider = Column(String(20), nullable=False)

    provider_user_id = Column(
        String(255),
        unique=True,
        nullable=False
    )

    email = Column(String(254), nullable=False)

    created_at = Column(DateTime)

    user = relationship("User")


class OTPLog(Base):
    __tablename__ = "accounts_otplog"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("accounts_user.id"),
        nullable=True
    )

    email = Column(String(254), nullable=False)

    otp = Column(String(6), nullable=False)

    is_verified = Column(Boolean, default=False)

    created_at = Column(DateTime)

    expires_at = Column(DateTime)

    user = relationship("User")