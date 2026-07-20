from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

from fastapi_app.notifications.service import add_notification

from .manager import manager
from .service import (
    save_private_message,
    save_group_message,
)

router = APIRouter()


@router.websocket("/ws/chat/{user_id}")
async def websocket_chat(websocket: WebSocket, user_id: str):

    await manager.connect(user_id, websocket)

    await manager.broadcast_online_users()

    try:

        while True:

            data = await websocket.receive_text()

            print("RAW DATA:", data)

            payload = json.loads(data)

            print("PAYLOAD:", payload)

            message = payload.get("message", "")
            receiver_id = payload.get("receiver_id")
            course_id = payload.get("course_id")
            is_group = payload.get("is_group", False)
            file = payload.get("file")

            if is_group:

                print("GROUP MESSAGE")

                await save_group_message(
                    sender_id=int(user_id),
                    course_id=course_id,
                    message=message,
                    file=file,
                )

                payload_data = json.dumps({
                    "sender_id": int(user_id),
                    "message": message,
                    "course_id": course_id,
                    "is_group": True,
                })

                print("BROADCASTING GROUP MESSAGE")

                await manager.broadcast(payload_data)
            else:

                print("PRIVATE MESSAGE")
                print("FROM:", user_id)
                print("TO:", receiver_id)
                print("MESSAGE:", message)

                await save_private_message(
                    sender_id=int(user_id),
                    receiver_id=int(receiver_id),
                    message=message,
                    file=file,
                )

                add_notification(
                    str(receiver_id),
                    f"New message from User {user_id}"
                )

                payload_data = json.dumps({
                    "sender_id": int(user_id),
                    "receiver_id": int(receiver_id),
                    "message": message,
                    "is_group": False,
                })

                print("SENDING TO RECEIVER")

                await manager.send_personal_message(
                    payload_data,
                    str(receiver_id),
                )

                print("SENDING TO SENDER")

                await manager.send_personal_message(
                    payload_data,
                    str(user_id),
                )

    except WebSocketDisconnect:

        print("DISCONNECTED:", user_id)

        manager.disconnect(user_id)

        await manager.broadcast_online_users()

    except Exception as e:

        print("WEBSOCKET ERROR:", e)