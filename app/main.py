from fastapi import FastAPI


@app.get("/", tags=["Health"])
async def root():
    return {"message": "App is running and healthy"}
