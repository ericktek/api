from pydantic import BaseModel

class OnlineClassCreate(BaseModel):
    title: str
    schedule: str
    course_id: int

class OnlineClassResponse(BaseModel):
    id: int
    title: str
    schedule: str
    class_link: str

    class Config:
        orm_mode = True
