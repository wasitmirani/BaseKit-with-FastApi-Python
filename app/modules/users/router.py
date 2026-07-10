from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.responses import success_response
from app.core.dependencies import get_current_active_superuser, get_current_user, get_db
from app.modules.users.model import User
from app.modules.users.schema import UserResponse, UserUpdate
from app.modules.users.service import UserService

router = APIRouter()


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


@router.get("/me", response_model=None)
def get_me(current_user: User = Depends(get_current_user)):
    return success_response(data=UserResponse.model_validate(current_user).model_dump())


@router.get("/")
def list_users(
    skip: int = 0,
    limit: int = 100,
    _: User = Depends(get_current_active_superuser),
    service: UserService = Depends(get_user_service),
):
    users = service.list_users(skip=skip, limit=limit)
    data = [UserResponse.model_validate(user).model_dump() for user in users]
    return success_response(data=data)


@router.get("/{user_id}")
def get_user(
    user_id: int,
    _: User = Depends(get_current_active_superuser),
    service: UserService = Depends(get_user_service),
):
    user = service.get_user(user_id)
    return success_response(data=UserResponse.model_validate(user).model_dump())


@router.patch("/{user_id}")
def update_user(
    user_id: int,
    payload: UserUpdate,
    _: User = Depends(get_current_active_superuser),
    service: UserService = Depends(get_user_service),
):
    user = service.update_user(user_id, payload)
    return success_response(data=UserResponse.model_validate(user).model_dump())


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    _: User = Depends(get_current_active_superuser),
    service: UserService = Depends(get_user_service),
):
    service.delete_user(user_id)
    return success_response(message="User deleted successfully")
