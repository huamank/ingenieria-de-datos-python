import logging
from retail_etl.logging_conf import setup_logging
from retail_etl.settings import get_settings
from retail_etl.db.mysql import get_mysql_engine
from retail_etl.db.mongo import get_mongo_db
from retail_etl.etl.pipeline import run_pipeline

def main() -> None:
    setup_logging()
    log = logging.getLogger("retail_etl")
    settings = get_settings()

    log.info("Starting retail ETL | env=%s", settings.app_env)

    mysql_engine = get_mysql_engine(settings.mysql_uri)
    mongo_db = get_mongo_db(settings.mongo_uri, settings.mongo_db)

    run_pipeline(settings, mysql_engine, mongo_db)

    log.info("ETL finished successfully.")