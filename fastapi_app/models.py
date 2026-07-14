from sqlalchemy import Column, Integer, String
from fastapi_app.database import Base


class User(Base):
    __tablename__ = "accounts_user"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(150), unique=True, index=True)

    full_name = Column(String(100))

    email = Column(String(254), unique=True, index=True)

    password = Column(String(128))

    role = Column(String(20))