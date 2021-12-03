from fastapi import FastAPI
from .views.docs import router as docsRouter

app = FastAPI()
app.include_router(docsRouter, tags=["docs"], prefix="/legal/v1/docs")

@app.get("/")
async def root():
    return {"message": "Welcome to the Legal World. Everything is per act and law!"}