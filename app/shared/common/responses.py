from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "Success"
    data: T | None = None


class PaginatedData(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    page_size: int
    pages: int


def success_response(data: Any = None, message: str = "Success") -> dict[str, Any]:
    return {"success": True, "message": message, "data": data}


def error_response(message: str, errors: Any = None) -> dict[str, Any]:
    return {"success": False, "message": message, "errors": errors}
