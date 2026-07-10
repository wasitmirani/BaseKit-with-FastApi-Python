import re

from pydantic import field_validator


def validate_password_strength(password: str) -> str:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not re.search(r"\d", password):
        raise ValueError("Password must contain at least one digit")
    return password


class PasswordValidatorMixin:
    @field_validator("password")
    @classmethod
    def password_strength(cls, value: str) -> str:
        return validate_password_strength(value)
