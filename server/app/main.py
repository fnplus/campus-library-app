from fastapi import FastAPI

from .routes import health, resources


def create_app() -> FastAPI:
    """Application factory to simplify testing."""
    app = FastAPI(title="CampusLibrary API", version="0.1.0")

    app.include_router(health.router)
    app.include_router(resources.router, prefix="/api")

    return app


app = create_app()
