from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

def get_mysql_engine(mysql_uri: str) -> Engine:
    # pool_pre_ping evita conexiones muertas
    return create_engine(mysql_uri, pool_pre_ping=True)