from fastapi import APIRouter
from courses.models import Course

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