from fastapi import APIRouter
from fastapi import APIRouter, HTTPException
from django.utils import timezone
from courses.models import Course, Plan, Subscription

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get("/")
def course_list():

    courses = Course.objects.all()

    data = []

    for course in courses:

        data.append(
            {
                "id": course.id,
                "title": course.title,
                "description": course.description,
                "status": course.status,
                "created_at": course.created_at,
            }
        )

    return data

@router.get("/{course_id}")
def course_details(course_id: int):

    try:
        course = Course.objects.get(id=course_id)

    except Course.DoesNotExist:
        return {
            "message": "Course not found"
        }

    return {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "status": course.status,
        "created_at": course.created_at,
    }

@router.get("/plans/")
def plan_list():

    plans = Plan.objects.all()

    data = []

    for plan in plans:

        data.append(
            {
                "id": plan.id,
                "name": plan.name,
                "price": float(plan.price),
                "duration_days": plan.duration_days,
            }
        )

    return data

@router.get("/premium/")
def premium_courses(user_id: int):

    today = timezone.now().date()

    expired_subscriptions = Subscription.objects.filter(
        user_id=user_id,
        status="active",
        end_date__lt=today
    )

    expired_subscriptions.update(status="expired")

    subscription = Subscription.objects.filter(
        user_id=user_id,
        status="active",
        end_date__gte=today
    ).first()
    
    if not subscription:
        raise HTTPException(
            status_code=403,
            detail="You don't have an active subscription."
        )

    courses = Course.objects.filter(is_premium=True)

    data = []

    for course in courses:
        data.append({
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "price": float(course.price),
        })

    return data