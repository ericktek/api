from fastapi import FastAPI
from app.config.database import engine, Base
from app.routers import auth_router, course_router, online_class_router

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Health check
@app.get("/", tags=["Health"])
async def read_root():
    return {"message": "Server is healthy"}


# Register the routers
app.include_router(auth_router.router, prefix="/auth")
app.include_router(course_router.router, prefix="/courses")
app.include_router(online_class_router.router, prefix="/online-classes")
