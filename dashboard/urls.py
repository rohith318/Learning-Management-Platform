from django.urls import path
from . import views
from . import user_views
from .views import chat_analytics, chat_page
from . import instructor_views
from django.http import HttpResponse
from .views import reports_view

urlpatterns = [

    # Admin Dashboard
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),

    # User
    path(
        "user/login/",
        user_views.user_login,
        name="user_login",
    ),

    path(
    "social-login-success/",
    user_views.social_login_success,
    name="social_login_success",
),

    path(
        "user/register/",
        user_views.register,
        name="register",
    ),

    path(
        "user/dashboard/",
        user_views.user_dashboard,
        name="user_dashboard",
    ),

    path(
        "user/courses/",
        user_views.my_courses,
        name="my_courses",
    ),

    path(
        "user/subscription/",
        user_views.subscription,
        name="subscription",
    ),

    path(
        "user/logout/",
        user_views.user_logout,
        name="user_logout",
    ),

    path(
    "notifications/",
    views.notification_list,
    name="notification_list",
),

path(
    "notifications/read/<int:notification_id>/",
    views.mark_notification_read,
    name="mark_notification_read",
),

path(
    "analytics/overview/",
    views.analytics_overview,
    name="analytics_overview",
),

path(
    "analytics/monthly/",
    views.analytics_monthly,
    name="analytics_monthly",
),


path(
    "chat-analytics/",
    chat_analytics,
    name="chat_analytics",
),

path(
    "chat/",
    chat_page,
    name="chat_page",
),

path(
    "instructor/dashboard/",
    instructor_views.instructor_dashboard,
    name="instructor_dashboard",
),

path(
    "instructor/attendance/",
    instructor_views.attendance_page,
    name="instructor_attendance",
),

path(
    "instructor/assignments/",
    instructor_views.assignments_page,
    name="instructor_assignments",
),

path(
    "instructor/submissions/",
    instructor_views.submissions_page,
    name="instructor_submissions",
),

path(
    "instructor/notifications/",
    instructor_views.notifications_page,
    name="instructor_notifications",
),

path(
    "instructor/my-courses/",
    instructor_views.instructor_courses,
    name="instructor_courses",
),

path(
    "instructor/assignments/create/",
    instructor_views.create_assignment,
    name="create_assignment",
),



path(
    "instructor/login/",
    instructor_views.instructor_login,
    name="instructor_login",
),

path(
    "user/assignments/",
    user_views.user_assignments,
    name="user_assignments",
),

path(
    "user/assignments/submit/<int:assignment_id>/",
    user_views.submit_assignment,
    name="submit_assignment",
),

path(
    "instructor/grade/<int:submission_id>/",
    instructor_views.grade_submission,
    name="grade_submission",
),

path(
    "instructor/reports/",
    reports_view,
    name="reports",
),

]



