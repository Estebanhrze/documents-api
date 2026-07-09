from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_versions():
    return {"message": "Versions"}