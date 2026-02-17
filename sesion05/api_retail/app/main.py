from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.logging import setup_logging

from app.api.v1.routers import (
    health_router,
    customers_router,
    products_router,
    orders_router,
    metrics_router,
)

setup_logging()

def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)

    # Routers versionados
    app.include_router(health_router, prefix="/api/v1")
    app.include_router(customers_router, prefix="/api/v1")
    app.include_router(products_router, prefix="/api/v1")
    app.include_router(orders_router, prefix="/api/v1")
    app.include_router(metrics_router, prefix="/api/v1")

    # Handler global básico de errores no controlados
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )

    return app

app = create_app()