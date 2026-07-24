from django.contrib import admin
from .models import User, SocialAccount, OTPLog


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "full_name",
        "email",
        "role",
        "is_active",
    )
    search_fields = (
        "username",
        "full_name",
        "email",
    )
    list_filter = (
        "role",
        "is_active",
    )


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "provider",
        "email",
        "created_at",
    )
    search_fields = (
        "email",
        "provider_user_id",
    )
    list_filter = (
        "provider",
        "created_at",
    )


@admin.register(OTPLog)
class OTPLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "otp",
        "is_verified",
        "created_at",
        "expires_at",
    )
    search_fields = (
        "email",
    )
    list_filter = (
        "is_verified",
        "created_at",
    )