from django.contrib import admin
from .models import Notification, ActivityLog, AnalyticsRecord


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "message",
        "is_read",
        "created_at",
    )
    list_filter = (
        "is_read",
        "created_at",
    )
    search_fields = (
        "user__username",
        "message",
    )
    ordering = ("-created_at",)


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "action_type",
        "created_at",
    )
    list_filter = (
        "action_type",
        "created_at",
    )
    search_fields = (
        "user__username",
        "action_detail",
    )
    ordering = ("-created_at",)


@admin.register(AnalyticsRecord)
class AnalyticsRecordAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "total_users",
        "active_subscriptions",
        "revenue",
        "popular_course",
    )
    search_fields = (
        "popular_course",
    )
    ordering = ("-date",)