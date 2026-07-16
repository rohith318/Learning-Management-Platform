from django.conf import settings
from django.db import models


class Course(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    is_premium = models.BooleanField(
        default=False
    )

    instructor_commission = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "instructor"},
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons"
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "student"},
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    enrolled_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user.full_name} - {self.course.title}"


class Progress(models.Model):
    enrollment = models.OneToOneField(
        Enrollment,
        on_delete=models.CASCADE
    )

    completed_lessons = models.PositiveIntegerField(default=0)
    progress_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"{self.enrollment.user.full_name} - {self.progress_percent}%"

class CompletedLesson(models.Model):

    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE
    )

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )

    completed_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            "enrollment",
            "lesson"
        )

    def __str__(self):
        return (
            f"{self.enrollment.user.full_name}"
            f" - {self.lesson.title}"
        )

class Plan(models.Model):
    PLAN_CHOICES = (
        ("Basic", "Basic"),
        ("Pro", "Pro"),
        ("Enterprise", "Enterprise"),
    )

    name = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES,
        unique=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    duration_days = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("expired", "Expired"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE
    )

    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    def __str__(self):
        return f"{self.user.full_name} - {self.plan.name}"


class Payment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.full_name} - ₹{self.amount}"