from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("instructor", "Instructor"),
        ("student", "Student"),
    )

    full_name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student"
    )

    def __str__(self):
        return self.full_name if self.full_name else self.username
    

    
class SocialAccount(models.Model):
    PROVIDER_CHOICES = (
        ("google", "Google"),
        ("facebook", "Facebook"),
        ("github", "GitHub"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="social_accounts"
    )

    provider = models.CharField(
        max_length=20,
        choices=PROVIDER_CHOICES
    )

    provider_user_id = models.CharField(
        max_length=255,
        unique=True
    )

    email = models.EmailField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.provider}"


class OTPLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="otp_logs",
        null=True,
        blank=True
    )

    email = models.EmailField()

    otp = models.CharField(
        max_length=6
    )

    is_verified = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    expires_at = models.DateTimeField()

    def __str__(self):
        return f"{self.email} ({'Verified' if self.is_verified else 'Pending'})"    