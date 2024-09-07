from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.course_schema import CourseCreate, CourseResponse
from app.models.course import Course
from app.config.database import get_db

router = APIRouter()

@router.post("/create", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course
