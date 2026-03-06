from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Test Case Generator")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Test Case Generator is running 🚀"}