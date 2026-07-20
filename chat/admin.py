from django.contrib import admin
from .models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sender",
        "receiver",
        "is_group",
        "created_at",
    )

    list_filter = (
        "is_group",
        "created_at",
    )

    search_fields = (
        "sender__username",
        "receiver__username",
        "message",
    )

    ordering = ("-created_at",)