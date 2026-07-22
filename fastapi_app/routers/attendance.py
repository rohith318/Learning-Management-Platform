from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from fastapi_app.database import get_db
from fastapi_app.models import Attendance
from fastapi_app.schemas import AttendanceMarkRequest
from datetime import date
from fastapi_app.notifications.service import add_notification

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/mark")
def mark_attendance(
    request: AttendanceMarkRequest,
    db: Session = Depends(get_db)
):
    for record in request.records:

        existing = db.query(Attendance).filter(
            Attendance.student_id == record.student_id,
            Attendance.course_id == request.course_id,
            Attendance.date == request.date
        ).first()

        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"Attendance already marked for Student ID {record.student_id}"
            )

        attendance = Attendance(
            student_id=record.student_id,
            course_id=request.course_id,
            date=request.date,
            status=record.status
        )

        db.add(attendance)

    db.commit()

    # Create notification for each student
    for record in request.records:
        add_notification(
            str(record.student_id),
            f"Attendance marked as {record.status} for {request.date}."
        )

    return {
        "message": "Attendance marked successfully."
    }

@router.get("/student/{student_id}")
def get_student_attendance(
    student_id: int,
    course_id: int,
    db: Session = Depends(get_db)
):
    attendance = db.query(Attendance).filter(
        Attendance.student_id == student_id,
        Attendance.course_id == course_id
    ).all()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="No attendance records found."
        )

    total_classes = len(attendance)
    present_count = sum(
        1 for record in attendance
        if record.status.lower() == "present"
    )

    percentage = round((present_count / total_classes) * 100, 2)

    return {
        "student_id": student_id,
        "course_id": course_id,
        "total_classes": total_classes,
        "present": present_count,
        "attendance_percentage": percentage,
        "records": attendance
    }

@router.get("/course/{course_id}")
def get_course_attendance(
    course_id: int,
    from_date: date,
    to_date: date,
    db: Session = Depends(get_db)
):
    attendance = db.query(Attendance).filter(
        Attendance.course_id == course_id,
        Attendance.date >= from_date,
        Attendance.date <= to_date
    ).all()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="No attendance records found."
        )

    return {
        "course_id": course_id,
        "from_date": from_date,
        "to_date": to_date,
        "total_records": len(attendance),
        "records": attendance
    }