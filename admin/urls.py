from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

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
        auth_views.LogoutView.as_view(),
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

    path("", include("dashboard.urls")),

    path("courses/", include("courses.urls")),
    path("users/", include("accounts.urls")),
]