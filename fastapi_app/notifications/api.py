from fastapi import APIRouter
from .service import notifications

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.get("/{user_id}")
def get_notifications(user_id: int):

    return {
        "user_id": user_id,
        "notifications": notifications.get(str(user_id), [])
    }