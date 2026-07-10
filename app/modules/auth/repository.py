from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.modules.auth.model import RefreshToken


class AuthRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_refresh_token(self, user_id: int, token: str, expires_at: datetime) -> RefreshToken:
        refresh_token = RefreshToken(
            user_id=user_id,
            token=token,
            expires_at=expires_at,
            created_at=datetime.now(timezone.utc),
        )
        self.db.add(refresh_token)
        self.db.commit()
        self.db.refresh(refresh_token)
        return refresh_token

    def get_refresh_token(self, token: str) -> RefreshToken | None:
        return self.db.query(RefreshToken).filter(RefreshToken.token == token).first()

    def revoke_refresh_token(self, token: str) -> None:
        record = self.get_refresh_token(token)
        if record:
            record.is_revoked = True
            self.db.commit()
