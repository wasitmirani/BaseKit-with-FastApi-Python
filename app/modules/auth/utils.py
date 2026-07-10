from datetime import datetime, timezone


def is_token_expired(expires_at: datetime) -> bool:
    return expires_at < datetime.now(timezone.utc)
