from django.shortcuts import render
from accounts.models import User
from django.contrib.auth.decorators import login_required
from courses.models import (
    Course,
    Lesson,
    Enrollment,
    Progress,
)


@login_required
def dashboard(request):

    context = {
        "total_users": User.objects.count(),
        "total_students": User.objects.filter(role="student").count(),
        "total_instructors": User.objects.filter(role="instructor").count(),
        "total_courses": Course.objects.count(),
        "total_lessons": Lesson.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
        "total_progress": Progress.objects.count(),

        "recent_courses": Course.objects.order_by("-created_at")[:5],
    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )