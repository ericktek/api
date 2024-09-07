from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.online_class_schema import OnlineClassCreate, OnlineClassResponse
from app.models.online_class import OnlineClass
from app.config.database import get_db
import random

router = APIRouter()

# For WebRTC, generate a basic link or use signaling servers.
def generate_webrtc_link():
    return f"https://webrtc.example.com/room/{random.randint(1000, 9999)}"

@router.post("/schedule", response_model=OnlineClassResponse)
def schedule_online_class(online_class: OnlineClassCreate, db: Session = Depends(get_db)):
    class_link = generate_webrtc_link()
    new_online_class = OnlineClass(
        title=online_class.title,
        schedule=online_class.schedule,
        class_link=class_link,
        course_id=online_class.course_id
    )
    db.add(new_online_class)
    db.commit()
    db.refresh(new_online_class)
    return new_online_class
