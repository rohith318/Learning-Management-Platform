notifications = {}


def add_notification(user_id: str, message: str):

    print(f"Notification Added -> {user_id} : {message}")

    if user_id not in notifications:
        notifications[user_id] = []

    notifications[user_id].append(
        {
            "title": "New Message",
            "message": message,
            "is_read": False
        }
    )


def get_notifications(user_id: str):
    return notifications.get(user_id, [])


def clear_notifications(user_id: str):
    notifications[user_id] = []