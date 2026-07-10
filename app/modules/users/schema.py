from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    full_name: str | None = None
    is_active: bool | None = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime

    model_config = {"from_attributes": True}
