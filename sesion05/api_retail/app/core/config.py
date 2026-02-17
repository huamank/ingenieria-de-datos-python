import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Settings centralizados (enterprise):
    - Lee variables desde .env
    - Arma la cadena de conexión MySQL
    """
    APP_NAME: str = os.getenv("APP_NAME", "Retail API (Enterprise)")
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    APP_HOST: str = os.getenv("APP_HOST", "127.0.0.1")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))

    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "root")
    DB_HOST: str = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT: int = int(os.getenv("DB_PORT", "3310"))
    DB_NAME: str = os.getenv("DB_NAME", "retail_db")

    @property
    def DATABASE_URL(self) -> str:
        # SQLAlchemy URL con PyMySQL
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()