from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_approvals():
    return {"message": "Approvals"}