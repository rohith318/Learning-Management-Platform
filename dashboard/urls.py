from django.urls import path
from . import views
from . import user_views

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

]