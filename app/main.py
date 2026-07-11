from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.APP_VERSION,
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "status": "running",
        "message": "Welcome to Documentex API",
        "version": settings.APP_VERSION
    }