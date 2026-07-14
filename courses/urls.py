from django.urls import path
from . import views

urlpatterns = [

    # Course URLs
    path("", views.course_list, name="course_list"),
    path("add/", views.add_course, name="add_course"),
    path("edit/<int:pk>/", views.edit_course, name="edit_course"),
    path("delete/<int:pk>/", views.delete_course, name="delete_course"),

    # Lesson URLs
    path("lessons/", views.lesson_list, name="lesson_list"),
    path("lessons/add/", views.add_lesson, name="add_lesson"),
    path("lessons/edit/<int:pk>/", views.edit_lesson, name="edit_lesson"),
    path("lessons/delete/<int:pk>/", views.delete_lesson, name="delete_lesson"),

    # Enrollment URLs
    path("enrollments/", views.enrollment_list, name="enrollment_list"),
    path("enrollments/add/", views.add_enrollment, name="add_enrollment"),
    path("enrollments/edit/<int:pk>/", views.edit_enrollment, name="edit_enrollment"),
    path("enrollments/delete/<int:pk>/", views.delete_enrollment, name="delete_enrollment"),

    # Progress URLs
    path("progress/", views.progress_list, name="progress_list"),
    path("progress/add/", views.add_progress, name="add_progress"),
    path("progress/edit/<int:pk>/", views.edit_progress, name="edit_progress"),
    path("progress/delete/<int:pk>/", views.delete_progress, name="delete_progress"),

    # Reports URL
    path("reports/", views.report_list, name="report_list"),
    path("reports/pdf/", views.download_report, name="download_report"),
]