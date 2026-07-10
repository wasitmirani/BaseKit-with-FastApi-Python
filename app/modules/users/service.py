from sqlalchemy.orm import Session

from app.common.exceptions import NotFoundException
from app.modules.users.model import User
from app.modules.users.repository import UserRepository
from app.modules.users.schema import UserUpdate


class UserService:
    def __init__(self, db: Session) -> None:
        self.repo = UserRepository(db)

    def get_user(self, user_id: int) -> User:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        return user

    def list_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.repo.list_all(skip=skip, limit=limit)

    def update_user(self, user_id: int, payload: UserUpdate) -> User:
        user = self.get_user(user_id)
        update_data = payload.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        return self.repo.update(user)

    def delete_user(self, user_id: int) -> None:
        user = self.get_user(user_id)
        self.repo.delete(user)
