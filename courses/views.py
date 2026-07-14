from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Lesson, Enrollment, Progress
from .forms import CourseForm, LessonForm, EnrollmentForm, ProgressForm
from accounts.models import User
from django.core.paginator import Paginator

from django.http import HttpResponse

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

def course_list(request):

    search = request.GET.get("search", "")

    courses = Course.objects.all()

    if search:
        courses = courses.filter(
            title__icontains=search
        )

    paginator = Paginator(courses, 5)

    page_number = request.GET.get("page")

    courses = paginator.get_page(page_number)

    return render(
        request,
        "courses/course_list.html",
        {
            "courses": courses,
            "search": search,
        },
    )


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()

    return render(request, "courses/course_form.html", {
        "form": form,
        "title": "Add Course"
    })


def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm(instance=course)

    return render(request, "courses/course_form.html", {
        "form": form,
        "title": "Edit Course"
    })


def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect("course_list")



def lesson_list(request):

    search = request.GET.get("search", "")

    lessons = Lesson.objects.select_related("course").all()

    if search:
        lessons = lessons.filter(
            title__icontains=search
        )

    paginator = Paginator(lessons, 5)

    page_number = request.GET.get("page")

    lessons = paginator.get_page(page_number)

    return render(
        request,
        "lessons/lesson_list.html",
        {
            "lessons": lessons,
            "search": search,
        },
    )


def add_lesson(request):
    if request.method == "POST":
        form = LessonForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lesson_list")

    else:
        form = LessonForm()

    return render(
        request,
        "lessons/lesson_form.html",
        {
            "form": form,
            "title": "Add Lesson",
        },
    )


def edit_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)

    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)

        if form.is_valid():
            form.save()
            return redirect("lesson_list")

    else:
        form = LessonForm(instance=lesson)

    return render(
        request,
        "lessons/lesson_form.html",
        {
            "form": form,
            "title": "Edit Lesson",
        },
    )


def delete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lesson.delete()

    return redirect("lesson_list")



def enrollment_list(request):

    search = request.GET.get("search", "")

    enrollments = Enrollment.objects.select_related(
        "user",
        "course"
    ).all()

    if search:
        enrollments = enrollments.filter(
            user__username__icontains=search
        )

    paginator = Paginator(enrollments, 5)

    page_number = request.GET.get("page")

    enrollments = paginator.get_page(page_number)

    return render(
        request,
        "enrollments/enrollment_list.html",
        {
            "enrollments": enrollments,
            "search": search,
        },
    )


def add_enrollment(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("enrollment_list")

    else:
        form = EnrollmentForm()

    return render(
        request,
        "enrollments/enrollment_form.html",
        {
            "form": form,
            "title": "Add Enrollment",
        },
    )


def edit_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=enrollment)

        if form.is_valid():
            form.save()
            return redirect("enrollment_list")

    else:
        form = EnrollmentForm(instance=enrollment)

    return render(
        request,
        "enrollments/enrollment_form.html",
        {
            "form": form,
            "title": "Edit Enrollment",
        },
    )


def delete_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    enrollment.delete()

    return redirect("enrollment_list")

def progress_list(request):

    search = request.GET.get("search", "")

    progress_list = Progress.objects.select_related(
        "enrollment__user",
        "enrollment__course"
    ).all()

    if search:
        progress_list = progress_list.filter(
            enrollment__user__username__icontains=search
        )

    paginator = Paginator(progress_list, 5)

    page_number = request.GET.get("page")

    progress_list = paginator.get_page(page_number)

    return render(
        request,
        "progress/progress_list.html",
        {
            "progress_list": progress_list,
            "search": search,
        },
    )

def add_progress(request):
    if request.method == "POST":
        form = ProgressForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("progress_list")

    else:
        form = ProgressForm()

    return render(
        request,
        "progress/progress_form.html",
        {
            "form": form,
            "title": "Add Progress",
        },
    )


def edit_progress(request, pk):
    progress = get_object_or_404(Progress, pk=pk)

    if request.method == "POST":
        form = ProgressForm(request.POST, instance=progress)

        if form.is_valid():
            form.save()
            return redirect("progress_list")

    else:
        form = ProgressForm(instance=progress)

    return render(
        request,
        "progress/progress_form.html",
        {
            "form": form,
            "title": "Edit Progress",
        },
    )


def delete_progress(request, pk):
    progress = get_object_or_404(Progress, pk=pk)
    progress.delete()

    return redirect("progress_list")

def report_list(request):

    context = {
        "total_users": User.objects.count(),
        "total_students": User.objects.filter(role="student").count(),
        "total_instructors": User.objects.filter(role="instructor").count(),
        "total_courses": Course.objects.count(),
        "total_lessons": Lesson.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
        "total_progress": Progress.objects.count(),
    }

    return render(
        request,
        "reports/report_list.html",
        context,
    )

def download_report(request):

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="LMS_Report.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Learning Management System Report</b>", styles["Title"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph(f"Total Users : {User.objects.count()}", styles["Normal"]))
    story.append(Paragraph(f"Total Students : {User.objects.filter(role='student').count()}", styles["Normal"]))
    story.append(Paragraph(f"Total Instructors : {User.objects.filter(role='instructor').count()}", styles["Normal"]))
    story.append(Paragraph(f"Total Courses : {Course.objects.count()}", styles["Normal"]))
    story.append(Paragraph(f"Total Lessons : {Lesson.objects.count()}", styles["Normal"]))
    story.append(Paragraph(f"Total Enrollments : {Enrollment.objects.count()}", styles["Normal"]))
    story.append(Paragraph(f"Total Progress Records : {Progress.objects.count()}", styles["Normal"]))

    doc.build(story)

    return response