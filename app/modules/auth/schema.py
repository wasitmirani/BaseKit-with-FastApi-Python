from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.common.validators import PasswordValidatorMixin


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RegisterRequest(PasswordValidatorMixin, BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str | None = None


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str
    exp: datetime
    type: str
