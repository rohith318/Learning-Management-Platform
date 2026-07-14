from fastapi import APIRouter, HTTPException

from accounts.models import User
from courses.models import Course, Enrollment

from fastapi_app.schemas import EnrollmentCreate

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


@router.post("/")
def enroll_course(data: EnrollmentCreate):

    try:
        user = User.objects.get(id=data.user_id)
    except User.DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    try:
        course = Course.objects.get(id=data.course_id)
    except Course.DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    if Enrollment.objects.filter(
        user=user,
        course=course
    ).exists():

        raise HTTPException(
            status_code=400,
            detail="Already enrolled"
        )

    enrollment = Enrollment.objects.create(
        user=user,
        course=course
    )

    return {
        "message": "Enrollment successful",
        "enrollment_id": enrollment.id,
        "student": user.full_name,
        "course": course.title,
    }