from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_documentsTypes():
    return {"message": "Document types"}