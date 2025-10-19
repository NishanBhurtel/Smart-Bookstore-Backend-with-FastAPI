from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserRead(UserCreate):
    id: int
    is_active: bool
