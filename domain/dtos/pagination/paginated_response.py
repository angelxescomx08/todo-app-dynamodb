from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    total_pages: int
    total_items: int
    next: Optional[int]
    previous: Optional[int]
    results: List[T]
