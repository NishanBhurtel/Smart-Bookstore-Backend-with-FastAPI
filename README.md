# Smart Bookstore Backend (FastAPI)

Minimal FastAPI backend for a bookstore. This repository contains a small, well-structured FastAPI project using SQLModel (SQLAlchemy + Pydantic).

Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app:

```bash
uvicorn app.main:app --reload
```

3. Open docs at http://127.0.0.1:8000/docs

Project layout

- `app/` — application package
  - `core/` — configuration
  - `db/` — database initialization and session
  - `api/` — routers and schemas
  - `models/` — database models

Next steps

- Add models and CRUD operations
- Add routers for books and users
- Add tests under `tests/`
# Smart-Bookstore-Backend-with-FastAPI .
