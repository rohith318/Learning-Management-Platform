from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ChatMessageCreate(BaseModel):
    sender_id: int
    receiver_id: Optional[int] = None
    course_id: Optional[int] = None
    message: str
    is_group: bool = False
    file_url: Optional[str] = None


class ChatMessageResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: Optional[int] = None
    course_id: Optional[int] = None
    message: str
    file_url: Optional[str] = None
    is_group: bool
    created_at: datetime

    class Config:
        from_attributes = True