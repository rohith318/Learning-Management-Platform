from django.db import models
from django.conf import settings


class ChatMessage(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )

    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
        null=True,
        blank=True
    )

    course_id = models.IntegerField(
        null=True,
        blank=True
    )

    message = models.TextField()

    file = models.FileField(
        upload_to="chat_files/",
        null=True,
        blank=True
    )

    is_group = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    last_seen = models.DateTimeField(
    null=True,
    blank=True
)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        if self.receiver:
            return f"{self.sender} → {self.receiver}"
        return f"{self.sender} → Group"