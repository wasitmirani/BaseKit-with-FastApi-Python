from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.responses import success_response
from app.core.dependencies import get_db
from app.modules.auth.schema import LoginRequest, RefreshTokenRequest, RegisterRequest
from app.modules.auth.service import AuthService

router = APIRouter()


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)


@router.post("/register")
def register(payload: RegisterRequest, service: AuthService = Depends(get_auth_service)):
    user = service.register(payload)
    return success_response(
        data={"id": user.id, "email": user.email, "full_name": user.full_name},
        message="User registered successfully",
    )


@router.post("/login")
def login(payload: LoginRequest, service: AuthService = Depends(get_auth_service)):
    tokens = service.login(payload)
    return success_response(data=tokens.model_dump(), message="Login successful")


@router.post("/refresh")
def refresh_token(payload: RefreshTokenRequest, service: AuthService = Depends(get_auth_service)):
    tokens = service.refresh(payload.refresh_token)
    return success_response(data=tokens.model_dump(), message="Token refreshed")
