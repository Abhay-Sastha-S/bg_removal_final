from fastapi import FastAPI
from .router import router

app = FastAPI(title="Background Removal API")

app.include_router(router, prefix="/api", tags=["background_removal"])

@app.get("/")
def root():
    return {"message": "Welcome to the Background Removal API!"}
