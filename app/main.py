from fastapi import FastAPI

from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

    @app.get("/health", tags=["health"])
    def health():
        return {"status": "ok", "project": settings.PROJECT_NAME}

    # include routers
    from app.api.v1.routers import books, users  # local import to avoid side-effects

    app.include_router(books.router)
    app.include_router(users.router)

    # initialize DB on startup
    from app.db.base import init_db


    @app.on_event("startup")
    def on_startup():
        init_db()

    return app


app = create_app()
