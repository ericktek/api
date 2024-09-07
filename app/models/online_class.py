from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class OnlineClass(Base):
    __tablename__ = 'online_classes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    schedule = Column(String)  # Store the scheduled time
    class_link = Column(String)  # WebRTC link
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Course")
