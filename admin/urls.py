from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dashboard.views import logout_view
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from dashboard.user_views import (
    user_login,
    user_dashboard,
    my_courses,
    user_logout,
)

from dashboard.user_views import (
    user_login,
    register,
    user_dashboard,
    my_courses,
    subscription,
    buy_plan,
    payment_success,
    payments,
    profile,
    edit_profile,
    download_invoice,
    user_logout,
    course_details,
    mark_lesson_complete,
     next_lesson,
     download_certificate,
     generate_certificate,
)

urlpatterns = [

    path("admin/", admin.site.urls),

    # Home → Login
    path(
        "",
        lambda request: redirect("login"),
        name="home",
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(),
        name="login",
    ),

    path(
    "logout/",
    logout_view,
    name="logout",
),


    path(
    "forgot-password/",
    auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html"
    ),
    name="password_reset",
),

path(
    "forgot-password/done/",
    auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"
    ),
    name="password_reset_done",
),

path(
    "user/login/",
    user_login,
    name="user_login",
),

path(
    "user/logout/",
    user_logout,
    name="user_logout",
),

path(
    "user/dashboard/",
    user_dashboard,
    name="user_dashboard",
),


path(
    "user/courses/",
    my_courses,
    name="my_courses",
),

path(
    "user/course/<int:course_id>/",
    course_details,
    name="course_details",
),

path(
    "user/subscription/",
    subscription,
    name="subscription",
),

path(
    "user/buy-plan/<int:plan_id>/",
    buy_plan,
    name="buy_plan",
),

path(
    "user/payment-success/",
    payment_success,
    name="payment_success",
),

path(
    "user/invoice/<int:payment_id>/",
    download_invoice,
    name="download_invoice",
),

path(
    "user/payments/",
    payments,
    name="payments",
),

path(
    "user/profile/",
    profile,
    name="profile",
),

path(
    "user/profile/edit/",
    edit_profile,
    name="edit_profile",
),

path(
    "lesson/<int:lesson_id>/complete/",
    mark_lesson_complete,
    name="mark_lesson_complete",
),

path(
    "lesson/<int:lesson_id>/next/",
    next_lesson,
    name="next_lesson",
),

path(
    "certificate/<int:course_id>/",
    download_certificate,
    name="download_certificate",
),

path(
    "certificate/download/<int:course_id>/",
    generate_certificate,
    name="generate_certificate",
),

path(
    "analytics/",
    include("analytics_app.urls"),
),

    path("", include("dashboard.urls")),

    path("courses/", include("courses.urls")),
    path("users/", include("accounts.urls")),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)