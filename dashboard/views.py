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
from django.db.models import Count
from chat.models import ChatMessage
from django.db.models.functions import TruncDate
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from courses.models import Course, Enrollment


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


    # ---------------- Chat Analytics ----------------

    total_chat_messages = ChatMessage.objects.count()

    private_messages = ChatMessage.objects.filter(
        is_group=False
    ).count()

    group_messages = ChatMessage.objects.filter(
        is_group=True
    ).count()

    today_messages = ChatMessage.objects.filter(
        created_at__date=today
    ).count()

    # Chat Messages Per Day (Last 7 Days)

    chat_data = (
        ChatMessage.objects
        .annotate(day=TruncDate("created_at"))
        .values("day")
        .annotate(total=Count("id"))
        .order_by("day")
    )

    chat_labels = []
    chat_counts = []

    for item in chat_data:
        chat_labels.append(item["day"].strftime("%d %b"))
        chat_counts.append(item["total"])

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

        "total_chat_messages": total_chat_messages,
        "private_messages": private_messages,
        "group_messages": group_messages,
        "today_messages": today_messages,
        "chat_labels": json.dumps(chat_labels),
        "chat_counts": json.dumps(chat_counts),
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

from django.shortcuts import render


def chat_analytics(request):

    private_count = ChatMessage.objects.filter(
        is_group=False
    ).count()

    group_count = ChatMessage.objects.filter(
        is_group=True
    ).count()

    context = {
        "private_count": private_count,
        "group_count": group_count,
    }

    return render(
        request,
        "dashboard/chat_analytics.html",
        context,
    )
@login_required
def chat_page(request):
    return render(
        request,
        "chat/chat.html",
    )

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):

    logout(request)

    return redirect("instructor_login")

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from courses.models import Course, Enrollment


@login_required
def reports_view(request):

    if request.user.role != "instructor":
        return HttpResponseForbidden("Access Denied")

    User = get_user_model()

    context = {
        "total_students": User.objects.filter(role="student").count(),
        "total_instructors": User.objects.filter(role="instructor").count(),
        "total_courses": Course.objects.count(),
        "active_courses": Course.objects.filter(status="active").count(),
        "inactive_courses": Course.objects.filter(status="inactive").count(),
        "total_enrollments": Enrollment.objects.count(),
    }

    return render(
        request,
        "instructor/reports.html",
        context,
    )

from django.http import HttpResponse

def who_am_i(request):
    if request.user.is_authenticated:
        return HttpResponse(f"""
        Username: {request.user.username}<br>
        Superuser: {request.user.is_superuser}<br>
        Staff: {request.user.is_staff}
        """)
    return HttpResponse("Anonymous User")



