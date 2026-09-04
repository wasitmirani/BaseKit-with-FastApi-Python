from math import ceil

from fastapi import Query
from pydantic import BaseModel
from sqlalchemy.orm import Query as SQLQuery

from app.core.constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE


class PaginationParams(BaseModel):
    page: int = 1
    page_size: int = DEFAULT_PAGE_SIZE

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size


def get_pagination_params(
    page: int = Query(1, ge=1),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE),
) -> PaginationParams:
    return PaginationParams(page=page, page_size=page_size)


def paginate(query: SQLQuery, page: int, page_size: int) -> tuple[list, int, int]:
    total = query.count()
    items = query.offset((page - 1) * page_size).limit(page_size).all()
    pages = ceil(total / page_size) if page_size else 0
    return items, total, pages
