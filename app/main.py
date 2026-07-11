from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "status": "running",
        "message": "Welcome to Documentex API"
    }