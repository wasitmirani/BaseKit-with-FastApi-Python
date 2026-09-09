from datetime import datetime, timezone
import secrets
import string


def utc_now() -> datetime:
    return datetime.now(timezone.utc)



def generate_random_string(length: int = 32) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def to_dict(obj, exclude: set[str] | None = None) -> dict:
    exclude = exclude or set()
    return {key: value for key, value in obj.__dict__.items() if key not in exclude and not key.startswith("_")}
