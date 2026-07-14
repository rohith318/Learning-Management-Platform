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