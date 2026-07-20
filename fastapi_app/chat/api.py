from fastapi import APIRouter
from asgiref.sync import sync_to_async

from chat.models import ChatMessage

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@sync_to_async
def fetch_history(sender_id: int, receiver_id: int):
    chats = ChatMessage.objects.filter(
        sender_id__in=[sender_id, receiver_id],
        receiver_id__in=[sender_id, receiver_id],
        is_group=False,
    ).order_by("created_at")

    return list(
        chats.values(
            "id",
            "sender_id",
            "receiver_id",
            "message",
            "created_at",
        )
    )


@router.get("/history/{sender_id}/{receiver_id}")
async def chat_history(sender_id: int, receiver_id: int):

    return await fetch_history(
        sender_id,
        receiver_id,
    )