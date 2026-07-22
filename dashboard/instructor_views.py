from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import requests

from courses.models import Course, Enrollment
from .decorators import instructor_required
from dashboard.models import Notification
from courses.models import Course
import requests
from django.contrib import messages


# ==========================
# Instructor Login
# ==========================

from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect


def instructor_login(request):

    if request.user.is_authenticated:
        if hasattr(request.user, "role") and request.user.role.lower() == "instructor":
            return redirect("instructor_dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is None:
            messages.error(request, "Invalid username or password.")
            return render(request, "instructor/login.html")

        if user.role.lower() != "instructor":
            messages.error(request, "Only instructors can login here.")
            return render(request, "instructor/login.html")

        login(request, user)
        messages.success(request, "Instructor Login Successful.")
        return redirect("instructor_dashboard")

    return render(
        request,
        "instructor/login.html"
    )
# ==========================
# Instructor Dashboard
# ==========================

@instructor_required
def instructor_dashboard(request):

    course_count = Course.objects.filter(
        instructor=request.user
    ).count()

    assignment_count = 0

    notification_count = 0

    context = {
        "course_count": course_count,
        "assignment_count": assignment_count,
        "notification_count": notification_count,
    }

    return render(
        request,
        "instructor/dashboard.html",
        context
    )
# ==========================
# My Courses
# ==========================

@instructor_required
def instructor_courses(request):

    courses = Course.objects.filter(
        instructor=request.user
    )

    return render(
        request,
        "instructor/my_courses.html",
        {
            "courses": courses
        }
    )


# ==========================
# Attendance
# ==========================

@instructor_required
def attendance_page(request):

    courses = Course.objects.filter(
        instructor=request.user
    )

    selected_course = request.GET.get("course")

    students = []

    if selected_course:

        students = Enrollment.objects.filter(
            course_id=selected_course
        ).select_related("user")

    return render(
        request,
        "instructor/attendance.html",
        {
            "courses": courses,
            "students": students,
            "selected_course": selected_course,
        }
    )


# ==========================
# Assignment List
# ==========================

@instructor_required
def assignments_page(request):

    assignments = []

    try:

        response = requests.get(
            "http://127.0.0.1:8001/assignments/"
        )

        if response.status_code == 200:
            assignments = response.json()

    except Exception as e:
        print(e)

    return render(
        request,
        "instructor/assignments.html",
        {
            "assignments": assignments
        }
    )


# ==========================
# Create Assignment
# ==========================

@instructor_required
def create_assignment(request):

    courses = Course.objects.filter(
        instructor=request.user
    )

    if request.method == "POST":

        try:

            assignment_file = request.FILES.get("file")

            files = {
                "file": (
                    assignment_file.name,
                    assignment_file,
                    assignment_file.content_type,
                )
            }

            data = {
                "course_id": request.POST.get("course_id"),
                "title": request.POST.get("title"),
                "description": request.POST.get("description"),
                "deadline": request.POST.get("deadline"),
                "created_by": request.user.id,
            }

            response = requests.post(
                "http://127.0.0.1:8001/assignments/create",
                data=data,
                files=files,
            )

            print("Status Code:", response.status_code)
            print("Response:", response.text)

            if response.status_code == 200:

                messages.success(
                    request,
                    "Assignment created successfully."
                )

                return redirect("instructor_assignments")

            messages.error(
                request,
                response.text
            )

        except Exception as e:

            messages.error(
                request,
                str(e)
            )

    return render(
        request,
        "instructor/create_assignment.html",
        {
            "courses": courses
        }
    )

# ==========================
# Assignment Submissions
# ==========================

@instructor_required
def submissions_page(request):

    return render(
        request,
        "instructor/submissions.html"
    )


# ==========================
# Notifications
# ==========================

@instructor_required
def notifications_page(request):

    notifications = []

    try:

        response = requests.get(
            f"http://127.0.0.1:8001/notifications/{request.user.id}"
        )

        print("Status Code:", response.status_code)
        print("Response:", response.text)

        if response.status_code == 200:

            notifications = response.json().get(
                "notifications",
                []
            )

            print("Notifications:", notifications)

    except Exception as e:

        print(e)

    return render(
        request,
        "instructor/notifications.html",
        {
            "notifications": notifications
        }
    )

@instructor_required
def grade_submission(request, submission_id):

    if request.method == "POST":

        grade = request.POST.get("grade")
        remarks = request.POST.get("remarks")

        response = requests.put(
            "http://127.0.0.1:8001/assignments/grade",
            params={
                "faculty_id": request.user.id
            },
            json={
                "submission_id": submission_id,
                "grade": grade,
                "remarks": remarks
            }
        )

        if response.status_code == 200:
            messages.success(
                request,
                "Assignment graded successfully."
            )
            return redirect("instructor_submissions")

        messages.error(
            request,
            response.text
        )

    return render(
        request,
        "instructor/grade_submission.html",
        {
            "submission_id": submission_id
        }
    )