from fastapi import WebSocket
from typing import Dict
import json


class ConnectionManager:

    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

        print(f"CONNECTED -> {user_id}")
        print(self.active_connections.keys())

    def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

        print(f"DISCONNECTED -> {user_id}")

    async def send_personal_message(self, message: str, user_id: str):

        print(f"SENDING TO -> {user_id}")
        print(message)

        websocket = self.active_connections.get(user_id)

        if websocket:
            print("FOUND CONNECTION")
            await websocket.send_text(message)
        else:
            print("CONNECTION NOT FOUND")

    async def broadcast(self, message: str):
        for websocket in self.active_connections.values():
            await websocket.send_text(message)

    def get_online_users(self):
        return list(self.active_connections.keys())

    async def broadcast_online_users(self):

        users = self.get_online_users()

        data = json.dumps({
            "type": "online_users",
            "users": users,
        })

        await self.broadcast(data)


manager = ConnectionManager()