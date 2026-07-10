from fastapi import Depends

from app.core.dependencies import get_current_user
from app.modules.users.model import User


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    return current_user
