import os
import shutil
from datetime import datetime
from fastapi_app.notifications.service import add_notification

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    File,
    Form,
)
from sqlalchemy.orm import Session

from fastapi_app.database import get_db
from fastapi_app.models import Assignment, Submission, User
from fastapi_app.schemas import GradeSubmissionRequest
from fastapi_app.models import User

router = APIRouter(
    prefix="/assignments",
    tags=["Assignments"]
)

UPLOAD_DIR = "uploads/assignments"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/create")
def create_assignment(
    course_id: int = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    deadline: datetime = Form(...),
    created_by: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    creator = db.query(User).filter(
        User.id == created_by
    ).first()

    if not creator:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    if creator.role.lower() not in ["faculty", "instructor"]:
        raise HTTPException(
            status_code=403,
            detail="Only faculty/instructors can create assignments."
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    assignment = Assignment(
        course_id=course_id,
        title=title,
        description=description,
        deadline=deadline,
        file_url=file_path,
        created_by=created_by,
    )

    db.add(assignment)
    db.commit()
    db.refresh(assignment)

    # Notification
    print("=" * 50)
    print("Creating Notification")
    print("Created By:", created_by)

    add_notification(
        str(created_by),
        f"Assignment '{title}' created successfully."
    )

    print("Current Notifications:")
    from fastapi_app.notifications.service import notifications
    print(notifications)
    print("=" * 50)

    return {
        "message": "Assignment created successfully.",
        "assignment_id": assignment.id,
    }

@router.post("/submit")
def submit_assignment(
    assignment_id: int = Form(...),
    student_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    assignment = db.query(Assignment).filter(
        Assignment.id == assignment_id
    ).first()

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found."
        )

    if datetime.now() > assignment.deadline:
        raise HTTPException(
            status_code=400,
            detail="Submission deadline has passed."
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        f"{student_id}_{file.filename}"
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    submission = Submission(
        assignment_id=assignment_id,
        student_id=student_id,
        file_url=file_path,
    )

    db.add(submission)
    db.commit()
    db.refresh(submission)

    return {
        "message": "Assignment submitted successfully.",
        "submission_id": submission.id
    }

@router.put("/grade")
def grade_submission(
    request: GradeSubmissionRequest,
    faculty_id: int,
    db: Session = Depends(get_db),
):
    faculty = db.query(User).filter(
        User.id == faculty_id
    ).first()

    if not faculty:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found."
        )

    if faculty.role.lower() not in ["faculty", "instructor"]:
        raise HTTPException(
            status_code=403,
            detail="Only faculty/instructors can grade submissions."
        )

    submission = db.query(Submission).filter(
        Submission.id == request.submission_id
    ).first()

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Submission not found."
        )

    submission.grade = request.grade
    submission.remarks = request.remarks

    db.commit()
    db.refresh(submission)

    # Create notification for student
    add_notification(
        str(submission.student_id),
        f"Your assignment has been graded. Grade: {request.grade}"
    )

    return {
        "message": "Assignment graded successfully.",
        "submission_id": submission.id,
        "grade": submission.grade,
        "remarks": submission.remarks,
    }

@router.get("/")
def get_assignments(db: Session = Depends(get_db)):

    assignments = db.query(Assignment).all()

    return [
        {
            "id": assignment.id,
            "course_id": assignment.course_id,
            "title": assignment.title,
            "description": assignment.description,
            "deadline": assignment.deadline,
            "file_url": assignment.file_url,
            "created_by": assignment.created_by,
        }
        for assignment in assignments
    ]

@router.get("/submissions")
def get_submissions(db: Session = Depends(get_db)):

    submissions = db.query(Submission).all()

    return [
        {
            "id": submission.id,
            "assignment_id": submission.assignment_id,
            "student_id": submission.student_id,
            "file_url": submission.file_url,
            "grade": submission.grade,
            "remarks": submission.remarks,
        }
        for submission in submissions
    ]