from fastapi import APIRouter

from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService

router = APIRouter()

service = UserService()


@router.get("/", response_model=list[UserResponse])
def get_users():
    return service.get_all()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    return service.get_by_id(user_id)


@router.post("/")
def create_user(user: UserCreate):
    return service.create(user.model_dump())


@router.put("/{user_id}")
def update_user(user_id: str, user: UserUpdate):
    return service.update(user_id, user.model_dump(exclude_unset=True))


@router.delete("/{user_id}")
def delete_user(user_id: str):
    return service.delete(user_id)