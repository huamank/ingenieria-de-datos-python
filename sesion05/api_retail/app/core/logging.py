import logging

def setup_logging() -> None:
    """
    Configuración simple de logging (enterprise-ready).
    Puedes evolucionar a JSON logging / structlog luego.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )