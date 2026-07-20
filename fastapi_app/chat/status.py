from fastapi import APIRouter
from .manager import manager

router = APIRouter(
    prefix="/chat",
    tags=["Chat Status"]
)


@router.get("/online-users")
def online_users():

    return {
        "online_users": manager.get_online_users()
    }