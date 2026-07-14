from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "full_name",
        "email",
        "role",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "role",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "full_name",
        "email",
    )

    ordering = ("id",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Learning Management",
            {
                "fields": (
                    "full_name",
                    "role",
                )
            },
        ),
    )