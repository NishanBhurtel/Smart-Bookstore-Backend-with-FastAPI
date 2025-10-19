from typing import List, Optional
from sqlmodel import select
from sqlmodel import Session

from app.models.book import Book


def create_book(db: Session, *, book: Book) -> Book:
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_book(db: Session, book_id: int) -> Optional[Book]:
    return db.get(Book, book_id)


def list_books(db: Session, offset: int = 0, limit: int = 100) -> List[Book]:
    statement = select(Book).offset(offset).limit(limit)
    return db.exec(statement).all()


def update_book(db: Session, book_id: int, data: dict) -> Optional[Book]:
    book = db.get(Book, book_id)
    if not book:
        return None
    for k, v in data.items():
        setattr(book, k, v)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int) -> bool:
    book = db.get(Book, book_id)
    if not book:
        return False
    db.delete(book)
    db.commit()
    return True
