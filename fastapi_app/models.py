from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from fastapi_app.database import Base


class User(Base):
    __tablename__ = "accounts_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, index=True)
    full_name = Column(String(100))
    email = Column(String(254), unique=True, index=True)
    password = Column(String(128))
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