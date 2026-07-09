from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="API para la gestión documental Documentex"
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