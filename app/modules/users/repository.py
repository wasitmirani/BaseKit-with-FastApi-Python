from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.modules.users.model import User


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def list_all(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.db.query(User).offset(skip).limit(limit).all()

    def create(self, user: User) -> User:
        now = datetime.now(timezone.utc)
        user.created_at = now
        user.updated_at = now
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user: User) -> User:
        user.updated_at = datetime.now(timezone.utc)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
