from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.common.exceptions import ConflictException, UnauthorizedException
from app.core.config import settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    get_password_hash,
    verify_password,
)
from app.modules.auth.repository import AuthRepository
from app.modules.auth.schema import LoginRequest, RegisterRequest, TokenResponse
from app.modules.users.model import User
from app.modules.users.repository import UserRepository


class AuthService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.user_repo = UserRepository(db)
        self.auth_repo = AuthRepository(db)

    def register(self, payload: RegisterRequest) -> User:
        if self.user_repo.get_by_email(payload.email):
            raise ConflictException("Email already registered")

        user = User(
            email=payload.email,
            hashed_password=get_password_hash(payload.password),
            full_name=payload.full_name,
        )
        return self.user_repo.create(user)

    def login(self, payload: LoginRequest) -> TokenResponse:
        user = self.user_repo.get_by_email(payload.email)
        if not user or not verify_password(payload.password, user.hashed_password):
            raise UnauthorizedException("Invalid email or password")

        return self._create_tokens(user)

    def refresh(self, refresh_token: str) -> TokenResponse:
        record = self.auth_repo.get_refresh_token(refresh_token)
        if not record or record.is_revoked or record.expires_at < datetime.now(timezone.utc):
            raise UnauthorizedException("Invalid refresh token")

        user = self.user_repo.get_by_id(record.user_id)
        if not user or not user.is_active:
            raise UnauthorizedException("User not found or inactive")

        return self._create_tokens(user)

    def _create_tokens(self, user: User) -> TokenResponse:
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        self.auth_repo.create_refresh_token(user.id, refresh_token, expires_at)

        return TokenResponse(access_token=access_token, refresh_token=refresh_token)
