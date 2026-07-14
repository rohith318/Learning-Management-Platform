from fastapi import APIRouter, HTTPException

from courses.models import Enrollment, Progress
from fastapi_app.schemas import ProgressCreate

router = APIRouter(
    prefix="/progress",
    tags=["Progress"]
)


@router.post("/")
def update_progress(data: ProgressCreate):

    try:
        enrollment = Enrollment.objects.get(
            id=data.enrollment_id
        )

    except Enrollment.DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    progress, created = Progress.objects.update_or_create(

        enrollment=enrollment,

        defaults={
            "completed_lessons": data.completed_lessons,
            "progress_percent": data.progress_percent,
        }
    )

    return {
        "message": "Progress Updated Successfully",
        "student": enrollment.user.full_name,
        "course": enrollment.course.title,
        "completed_lessons": progress.completed_lessons,
        "progress_percent": progress.progress_percent,
    }


@router.get("/{user_id}")
def view_progress(user_id: int):

    progress = Progress.objects.filter(
        enrollment__user_id=user_id
    )

    data = []

    for item in progress:

        data.append({
            "student": item.enrollment.user.full_name,
            "course": item.enrollment.course.title,
            "completed_lessons": item.completed_lessons,
            "progress_percent": float(item.progress_percent),
        })

    return data