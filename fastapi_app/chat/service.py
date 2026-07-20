from asgiref.sync import sync_to_async

from accounts.models import User
from chat.models import ChatMessage
from dashboard.models import Notification

@sync_to_async
def save_private_message(sender_id, receiver_id, message, file=None):

    sender = User.objects.get(id=sender_id)
    receiver = User.objects.get(id=receiver_id)

    chat = ChatMessage.objects.create(
        sender=sender,
        receiver=receiver,
        message=message,
        file=file,
        is_group=False,
    )

    Notification.objects.create(
        user=receiver,
        message=f"{sender.full_name}: {message}"
    )

    return chat


@sync_to_async
def save_group_message(sender_id, course_id, message, file=None):

    sender = User.objects.get(id=sender_id)

    chat = ChatMessage.objects.create(
        sender=sender,
        course_id=course_id,
        message=message,
        file=file,
        is_group=True,
    )

    return chat

@sync_to_async
def get_chat_history(sender_id, receiver_id):

    chats = ChatMessage.objects.filter(
        sender_id__in=[sender_id, receiver_id],
        receiver_id__in=[sender_id, receiver_id],
        is_group=False,
    ).order_by("created_at")

    return list(chats.values())