from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import User
from django.shortcuts import get_object_or_404
from datetime import timedelta
from django.utils import timezone
import stripe
from django.conf import settings
from django.http import FileResponse
import io
from django.http import HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

from courses.models import (
    Course,
    Lesson,
    Enrollment,
    Progress,
    Subscription,
    Payment,
    Plan,
    CompletedLesson,
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

def user_login(request):

    # If user is already logged in
    if request.user.is_authenticated:
        return redirect("user_dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                "Login Successful!"
            )

            return redirect("user_dashboard")

        else:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(
        request,
        "user/login.html",
    )


def register(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("register")

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("register")

        if User.objects.filter(email=email).exists():

            messages.error(
                request,
                "Email already exists."
            )

            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            full_name=full_name,
            role="student",
        )

        messages.success(
            request,
            "Account created successfully. Please log in."
        )

        return redirect("user_login")

    return render(
        request,
        "user/register.html",
    )


@login_required
def user_dashboard(request):

    user = request.user

    total_courses = Enrollment.objects.filter(
        user=user
    ).count()

    completed_courses = Progress.objects.filter(
        enrollment__user=user,
        progress_percent=100
    ).count()

    total_payments = Payment.objects.filter(
        user=user
    ).count()

    active_subscription = Subscription.objects.filter(
        user=user,
        status="active"
    ).first()

    recent_courses = Course.objects.order_by(
        "-created_at"
    )[:3]

    context = {
        "total_courses": total_courses,
        "completed_courses": completed_courses,
        "total_payments": total_payments,
        "active_subscription": active_subscription,
        "recent_courses": recent_courses,
    }

    return render(
        request,
        "user/dashboard.html",
        context,
    )


@login_required
def my_courses(request):

    enrollments = (
        Enrollment.objects
        .filter(user=request.user)
        .select_related("course")
    )

    context = {
        "enrollments": enrollments,
    }

    return render(
        request,
        "user/courses.html",
        context,
    )


@login_required
def user_logout(request):

    logout(request)

    return redirect("user_login")

@login_required
def subscription(request):

    subscription = Subscription.objects.filter(
        user=request.user,
        status="active"
    ).select_related("plan").first()

    plans = Plan.objects.all()

    context = {
        "subscription": subscription,
        "plans": plans,
    }

    return render(
        request,
        "user/subscription.html",
        context,
    )

@login_required
def buy_plan(request, plan_id):

    plan = get_object_or_404(
        Plan,
        id=plan_id
    )

    checkout_session = stripe.checkout.Session.create(

        payment_method_types=["card"],

        line_items=[
            {
                "price_data": {
                    "currency": "inr",
                    "product_data": {
                        "name": plan.name,
                    },
                    "unit_amount": int(plan.price * 100),
                },
                "quantity": 1,
            }
        ],

        mode="payment",

        success_url=request.build_absolute_uri(
            "/user/payment-success/"
        ) + f"?plan_id={plan.id}",

        cancel_url=request.build_absolute_uri(
            "/user/subscription/"
        ),
    )

    return redirect(
        checkout_session.url,
        code=303
    )

@login_required
def payments(request):

    payments = Payment.objects.filter(
        user=request.user
    ).select_related("plan")

    context = {
        "payments": payments,
    }

    return render(
        request,
        "user/payments.html",
        context,
    )

@login_required
def profile(request):

    return render(
        request,
        "user/profile.html",
    )

@login_required
def edit_profile(request):

    if request.method == "POST":

        request.user.full_name = request.POST.get("full_name")
        request.user.email = request.POST.get("email")

        request.user.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect("profile")

    return render(
        request,
        "user/edit_profile.html"
    )

@login_required
def payment_success(request):

    plan_id = request.GET.get("plan_id")

    plan = get_object_or_404(
        Plan,
        id=plan_id
    )

    Subscription.objects.filter(
        user=request.user
    ).delete()

    start_date = timezone.now().date()

    end_date = start_date + timedelta(
        days=plan.duration_days
    )

    Subscription.objects.create(
        user=request.user,
        plan=plan,
        start_date=start_date,
        end_date=end_date,
        status="active",
    )

    Payment.objects.create(
        user=request.user,
        plan=plan,
        amount=plan.price,
    )

    return render(
    request,
    "user/payment_success.html",
    {
        "subscription": Subscription.objects.get(user=request.user),
        "payment": Payment.objects.filter(
            user=request.user
        ).latest("payment_date"),
    },
)

@login_required
def download_invoice(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        user=request.user
    )

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>LearnPro Invoice</b>", styles["Title"])
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>Invoice ID:</b> INV-{payment.id}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Student:</b> {payment.user.full_name}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Plan:</b> {payment.plan.name}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Amount:</b> ₹{payment.amount}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Payment Date:</b> {payment.payment_date.strftime('%d-%m-%Y %I:%M %p')}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>Status : PAID</b>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1,30))

    story.append(
        Paragraph(
            "Thank you for purchasing LearnPro Subscription.",
            styles["Normal"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename=f"Invoice_{payment.id}.pdf"
    )

@login_required
def course_details(request, course_id):

    enrollment = Enrollment.objects.filter(
        user=request.user,
        course_id=course_id,
    ).first()

    if enrollment is None:
        return HttpResponse(
            f"No enrollment found.<br>"
            f"Logged in User: {request.user}<br>"
            f"Course ID: {course_id}"
        )

    course = enrollment.course

    lessons = Lesson.objects.filter(
        course=course
    )

    progress, created = Progress.objects.get_or_create(
        enrollment=enrollment
    )

    selected_lesson = lessons.first()

    context = {
        "course": course,
        "lessons": lessons,
        "progress": progress,
        "selected_lesson": selected_lesson,
    }

    return render(
        request,
        "user/course_details.html",
        context,
    )

@login_required
def mark_lesson_complete(request, lesson_id):

    lesson = get_object_or_404(
        Lesson,
        id=lesson_id
    )

    enrollment = get_object_or_404(
        Enrollment,
        user=request.user,
        course=lesson.course
    )

    completed, created = CompletedLesson.objects.get_or_create(
        enrollment=enrollment,
        lesson=lesson
    )

    progress, created_progress = Progress.objects.get_or_create(
        enrollment=enrollment
    )

    total_lessons = Lesson.objects.filter(
        course=lesson.course
    ).count()

    completed_count = CompletedLesson.objects.filter(
        enrollment=enrollment
    ).count()

    progress.completed_lessons = completed_count

    progress.progress_percent = (
        completed_count / total_lessons
    ) * 100

    progress.save()

    messages.success(
        request,
        "Lesson marked as completed!"
    )

    return redirect(
        "course_details",
        course_id=lesson.course.id
    )

@login_required
def next_lesson(request, lesson_id):

    current_lesson = get_object_or_404(
        Lesson,
        id=lesson_id
    )

    lessons = list(
        Lesson.objects.filter(
            course=current_lesson.course
        ).order_by("id")
    )

    try:
        current_index = lessons.index(current_lesson)

        next_lesson = lessons[current_index + 1]

        return redirect(
            "course_details",
            course_id=current_lesson.course.id,
        )

    except IndexError:

        messages.success(
            request,
            "🎉 Course Completed!"
        )

        return redirect(
            "course_details",
            course_id=current_lesson.course.id,
        )
    
@login_required
def download_certificate(request, course_id):

    enrollment = get_object_or_404(
        Enrollment,
        user=request.user,
        course_id=course_id
    )

    progress = get_object_or_404(
        Progress,
        enrollment=enrollment
    )

    if progress.progress_percent < 100:

        messages.error(
            request,
            "Complete the course to download the certificate."
        )

        return redirect(
            "course_details",
            course_id=course_id
        )

    return download_invoice(request, enrollment.id)

@login_required
def generate_certificate(request, course_id):

    enrollment = get_object_or_404(
        Enrollment,
        user=request.user,
        course_id=course_id
    )

    progress = get_object_or_404(
        Progress,
        enrollment=enrollment
    )

    if progress.progress_percent < 100:

        messages.error(
            request,
            "Complete the course first."
        )

        return redirect(
            "course_details",
            course_id=course_id
        )

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<font size='24'><b>🏆 CERTIFICATE OF COMPLETION</b></font>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 30))

    story.append(
        Paragraph(
            "This Certificate is proudly presented to",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            f"<font size='20'><b>{request.user.full_name}</b></font>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"For successfully completing the course <b>{enrollment.course.title}</b>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Completion Date : {timezone.now().strftime('%d %B %Y')}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 40))

    story.append(
        Paragraph(
            "<b>LearnPro Online Learning Platform</b>",
            styles["Heading2"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename="Certificate.pdf"
    ) 