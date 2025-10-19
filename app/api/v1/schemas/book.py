from typing import Optional
from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: float = 0.0
    in_stock: int = 0


class BookRead(BookCreate):
    id: int


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[int] = None
