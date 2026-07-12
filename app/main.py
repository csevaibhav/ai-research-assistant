from fastapi import FastAPI

from app.api.chat_api import router as chat_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API for an Agentic AI Research Assistant",
    version=settings.APP_VERSION,
)

app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Research Assistant 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }