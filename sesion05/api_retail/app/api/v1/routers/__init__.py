from .health import router as health_router
from .customers import router as customers_router
from .products import router as products_router
from .orders import router as orders_router
from .metrics import router as metrics_router

__all__ = [
    "health_router",
    "customers_router",
    "products_router",
    "orders_router",
    "metrics_router",
]