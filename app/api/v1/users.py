from fastapi import APIRouter

from app.services.user_service import UserService

router = APIRouter()

service = UserService()


@router.get("/")
def get_users():
    return service.get_all()


@router.get("/{user_id}")
def get_user(user_id: int):
    return service.get_by_id(user_id)


@router.post("/")
def create_user(user: dict):
    return service.create(user)


@router.put("/{user_id}")
def update_user(user_id: int, user: dict):
    return service.update(user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: int):
    return service.delete(user_id)