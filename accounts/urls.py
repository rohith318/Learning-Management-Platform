from django.urls import path
from . import views
from . import views
from dashboard.user_views import (
    user_login,
    user_dashboard,
    my_courses,
    user_logout,
    register,
    otp_login,
)

urlpatterns = [
    path("", views.user_list, name="user_list"),
    path("add/", views.add_user, name="add_user"),
    path("edit/<int:pk>/", views.edit_user, name="edit_user"),
    path("delete/<int:pk>/", views.delete_user, name="delete_user"),
    path(
    "forgot-password/",
    views.forgot_password,
    name="forgot_password",
),

path(
    "user/register/",
    register,
    name="register",
),

path(
    "user/otp-login/",
    otp_login,
    name="otp_login",
),

]