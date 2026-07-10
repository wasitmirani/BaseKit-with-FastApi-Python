from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.router import api_router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging
from app.core.middleware import register_middleware
from app.db.init_db import init_db
from app.websocket.routes import router as websocket_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    if settings.ENVIRONMENT != "test":
        init_db()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
        docs_url=f"{settings.API_V1_PREFIX}/docs",
        redoc_url=f"{settings.API_V1_PREFIX}/redoc",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_middleware(app)
    register_exception_handlers(app)

    app.include_router(api_router, prefix=settings.API_V1_PREFIX)
    app.include_router(websocket_router)

    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    @app.get("/health", tags=["health"])
    async def health_check():
        return {"status": "ok", "version": settings.VERSION}

    return app


app = create_app()
