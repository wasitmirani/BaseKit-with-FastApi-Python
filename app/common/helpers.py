from datetime import datetime, timezone


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def to_dict(obj, exclude: set[str] | None = None) -> dict:
    exclude = exclude or set()
    return {key: value for key, value in obj.__dict__.items() if key not in exclude and not key.startswith("_")}
