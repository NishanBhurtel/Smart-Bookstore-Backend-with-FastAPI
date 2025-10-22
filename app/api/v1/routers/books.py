from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.crud.book import create_book, get_book, list_books, update_book, delete_book
from app.api.v1.schemas.book import BookCreate, BookRead, BookUpdate
from app.models.book import Book
from sqlmodel import select

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create(book_in: BookCreate, db: Session = Depends(get_session)):
    book = Book.from_orm(book_in)
    return create_book(db, book=book)


@router.get("/", response_model=List[BookRead])
def read_list(offset: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return list_books(db, offset=offset, limit=limit)


@router.get("/search", response_model=List[BookRead])
def search(q: str, db: Session = Depends(get_session)):
    statement = select(Book).where((Book.title.contains(q)) | (Book.author.contains(q)))
    return db.exec(statement).all()


@router.get("/{book_id}", response_model=BookRead)
def read(book_id: int, db: Session = Depends(get_session)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.patch("/{book_id}", response_model=BookRead)
def patch(book_id: int, book_in: BookUpdate, db: Session = Depends(get_session)):
    data = book_in.dict(exclude_unset=True)
    book = update_book(db, book_id, data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(book_id: int, db: Session = Depends(get_session)):
    ok = delete_book(db, book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Book not found")
    return None


@router.post("/{book_id}/purchase", response_model=BookRead)
def purchase(book_id: int, quantity: int = 1, db: Session = Depends(get_session)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.in_stock < quantity:
        raise HTTPException(status_code=400, detail="Not enough stock")
    book.in_stock -= quantity
    db.add(book)
    db.commit()
    db.refresh(book)
    return book
