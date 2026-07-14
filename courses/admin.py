from django.contrib import admin
from .models import Course, Lesson, Enrollment, Progress


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "instructor",
        "status",
        "created_at",
    )
    search_fields = (
        "title",
        "instructor__username",
    )
    list_filter = (
        "status",
        "created_at",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "course",
    )
    search_fields = (
        "title",
        "course__title",
    )


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "course",
        "enrolled_on",
    )
    search_fields = (
        "user__username",
        "course__title",
    )


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "enrollment",
        "completed_lessons",
        "progress_percent",
    )