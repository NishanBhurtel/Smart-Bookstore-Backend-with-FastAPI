from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.crud.user import create_user, get_user_by_id, get_user_by_email
from app.api.v1.schemas.user import UserCreate, UserRead
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create(user_in: UserCreate, db: Session = Depends(get_session)):
    existing = get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=user_in.email, full_name=user_in.full_name)
    return create_user(db, user=user)


@router.get("/{user_id}", response_model=UserRead)
def read(user_id: int, db: Session = Depends(get_session)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/by_email", response_model=UserRead)
def by_email(email: str, db: Session = Depends(get_session)):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
