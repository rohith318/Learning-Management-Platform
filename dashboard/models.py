from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Notification(models.Model):
    """
    Stores in-app notifications for users.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.message[:30]}"


class ActivityLog(models.Model):
    """
    Tracks important user activities.
    """

    ACTION_CHOICES = [
        ("ENROLLMENT", "Enrollment"),
        ("COMPLETION", "Completion"),
        ("LOGIN", "Login"),
        ("LOGOUT", "Logout"),
        ("PAYMENT", "Payment"),
        ("OTHER", "Other"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="activity_logs"
    )
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICES)
    action_detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.action_type}"


class AnalyticsRecord(models.Model):
    """
    Stores daily analytics snapshots.
    """

    date = models.DateField(unique=True)
    total_users = models.PositiveIntegerField(default=0)
    active_subscriptions = models.PositiveIntegerField(default=0)
    revenue = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    popular_course = models.CharField(
        max_length=255,
        blank=True
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Analytics - {self.date}"