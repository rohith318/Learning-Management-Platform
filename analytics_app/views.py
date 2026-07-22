from django.http import JsonResponse
from accounts.models import User

from fastapi_app.database import SessionLocal
from fastapi_app.models import Attendance, Assignment, Submission


def analytics_dashboard(request):
    course_id = request.GET.get("course_id")

    db = SessionLocal()

    try:
        total_students = User.objects.filter(role="student").count()

        attendance_query = db.query(Attendance)

        if course_id:
            attendance_query = attendance_query.filter(
                Attendance.course_id == int(course_id)
            )

        attendance_records = attendance_query.all()

        total_records = len(attendance_records)

        present_records = len([
            record for record in attendance_records
            if record.status.lower() == "present"
        ])

        avg_attendance = (
            round((present_records / total_records) * 100, 2)
            if total_records
            else 0
        )

        assignment_query = db.query(Assignment)

        if course_id:
            assignment_query = assignment_query.filter(
                Assignment.course_id == int(course_id)
            )

        total_assignments = assignment_query.count()

        submissions_count = db.query(Submission).count()

        return JsonResponse({
            "total_students": total_students,
            "avg_attendance": avg_attendance,
            "total_assignments": total_assignments,
            "submissions_count": submissions_count,
        })

    finally:
        db.close()