from django.shortcuts import render
from accounts.models import User
from django.contrib.auth.decorators import login_required
from courses.models import (
    Course,
    Lesson,
    Enrollment,
    Progress,
    Payment,
)
from django.db.models import Sum, Count
from django.utils import timezone
from dashboard.models import ActivityLog
from django.contrib.auth import get_user_model
from .models import Notification
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth
import json
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):

    today = timezone.now().date()

    monthly_revenue = (
        Payment.objects.filter(payment_date__month=today.month)
        .aggregate(total=Sum("amount"))["total"]
        or 0
    )

    # Monthly revenue for chart
    monthly_data = (
        Payment.objects
        .annotate(month=ExtractMonth("payment_date"))
        .values("month")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )

    revenue_by_month = [0] * 12

    for item in monthly_data:
        revenue_by_month[item["month"] - 1] = float(item["total"])

    popular_courses = (
        Course.objects.annotate(
            total_enrollments=Count("enrollment")
        )
        .order_by("-total_enrollments")[:5]
    )

    max_enrollments = max(
    [course.total_enrollments for course in popular_courses],
    default=1
)

    for course in popular_courses:
        course.progress = int(
            (course.total_enrollments / max_enrollments) * 100
        )

    recent_activity = (
        ActivityLog.objects.select_related("user")
        .order_by("-created_at")[:10]
    )

    latest_notifications = (
        Notification.objects.filter(user=request.user)
        .order_by("-created_at")[:5]
    )

    notifications_count = (
        Notification.objects.filter(
            user=request.user,
            is_read=False
        ).count()
    )

    context = {
        "total_users": User.objects.count(),
        "total_students": User.objects.filter(role="student").count(),
        "total_instructors": User.objects.filter(role="instructor").count(),
        "total_courses": Course.objects.count(),
        "total_lessons": Lesson.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
        "total_progress": Progress.objects.count(),

        "monthly_revenue": monthly_revenue,
        "revenue_by_month": json.dumps(revenue_by_month),
        "popular_courses": popular_courses,
        "recent_activity": recent_activity,
        "latest_notifications": latest_notifications,
        "notifications_count": notifications_count,
        "recent_courses": Course.objects.order_by("-created_at")[:5],
    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(
        user=request.user
    ).order_by("-created_at")

    data = []

    for notification in notifications:
        data.append({
            "id": notification.id,
            "title": notification.title,
            "message": notification.message,
            "is_read": notification.is_read,
            "created_at": notification.created_at.strftime("%d-%m-%Y %H:%M"),
        })

    return JsonResponse(data, safe=False)

@require_POST
@login_required
def mark_notification_read(request, notification_id):
    try:
        notification = Notification.objects.get(
            id=notification_id,
            user=request.user
        )

        notification.is_read = True
        notification.save()

        return JsonResponse({
            "status": "success",
            "message": "Notification marked as read."
        })

    except Notification.DoesNotExist:

        return JsonResponse({
            "status": "error",
            "message": "Notification not found."
        }, status=404)
    

    from django.http import JsonResponse

@login_required
def analytics_overview(request):

    data = {
        "total_users": User.objects.count(),
        "total_students": User.objects.filter(role="student").count(),
        "total_instructors": User.objects.filter(role="instructor").count(),
        "total_courses": Course.objects.count(),
        "total_lessons": Lesson.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
        "total_progress": Progress.objects.count(),
        "monthly_revenue": Payment.objects.aggregate(
            total=Sum("amount")
        )["total"] or 0,
    }

    return JsonResponse(data)

@login_required
def analytics_monthly(request):

    monthly_data = (
        Payment.objects
        .annotate(month=ExtractMonth("payment_date"))
        .values("month")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )

    data = []

    for item in monthly_data:
        data.append({
            "month": item["month"],
            "revenue": float(item["total"]),
        })

    return JsonResponse(data, safe=False)

@login_required
def report(request):

    context = {
        "total_users": User.objects.count(),
        "total_courses": Course.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
        "total_payments": Payment.objects.count(),
        "total_revenue": Payment.objects.aggregate(
            total=Sum("amount")
        )["total"] or 0,
    }

    return render(
        request,
        "dashboard/report.html",
        context,
    )
