from fastapi import APIRouter
from .service import notifications
from fastapi import HTTPException

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

@router.post("/mark-read")
def mark_notification_read(
    user_id: int,
    notification_index: int
):
    user_key = str(user_id)

    if user_key not in notifications:
        raise HTTPException(
            status_code=404,
            detail="Notifications not found."
        )

    if notification_index < 0 or notification_index >= len(notifications[user_key]):
        raise HTTPException(
            status_code=404,
            detail="Notification not found."
        )

    notifications[user_key][notification_index]["is_read"] = True

    return {
        "message": "Notification marked as read."
    }