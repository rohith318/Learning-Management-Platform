from fastapi import APIRouter
from accounts.models import User
from asgiref.sync import sync_to_async

from fastapi_app.chat.manager import manager

router = APIRouter(
    prefix="/chat",
    tags=["Chat Users"],
)


@sync_to_async
def get_users():

    online_users = manager.get_online_users()

    users = []

    for user in User.objects.all():

        users.append(
    {
        "id": user.id,
        "full_name": user.full_name,
        "role": user.role,
        "online": str(user.id) in online_users,
    }
)
    return users


@router.get("/users")
async def chat_users():

    return await get_users()