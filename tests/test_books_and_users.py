from fastapi.testclient import TestClient

from app.main import app


def test_books_and_users_flow():
    client = TestClient(app)

    # create a user
    r = client.post("/users/", json={"email": "alice@example.com", "full_name": "Alice"})
    assert r.status_code == 201
    user = r.json()
    assert user["email"] == "alice@example.com"

    # create a book
    r = client.post("/books/", json={"title": "FastAPI 101", "author": "Bob", "price": 9.99, "in_stock": 3})
    assert r.status_code == 201
    book = r.json()
    book_id = book["id"]

    # search for the book
    r = client.get("/books/search", params={"q": "FastAPI"})
    assert r.status_code == 200
    assert any(b["id"] == book_id for b in r.json())

    # purchase 2 copies
    r = client.post(f"/books/{book_id}/purchase", params={"quantity": 2})
    assert r.status_code == 200
    assert r.json()["in_stock"] == 1

    # purchase too many
    r = client.post(f"/books/{book_id}/purchase", params={"quantity": 5})
    assert r.status_code == 400

    # lookup user by email
    r = client.get("/users/by_email", params={"email": "alice@example.com"})
    assert r.status_code == 200
    assert r.json()["email"] == "alice@example.com"
