from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from src.config import ENV

DATABASE_URL = URL.create(
    "postgresql+psycopg2",
    username=ENV["POSTGRES_USER"],
    password=ENV["POSTGRES_PASSWORD"],
    host=ENV["POSTGRES_HOST"],
    port=ENV["POSTGRES_PORT"],
    database=ENV["POSTGRES_DB"],
)

DATABASE_PARAMS = {
    "pool_pre_ping": True,
    "echo": False,
    "pool_size": 10,
    "max_overflow": 50,
}

engine = create_engine(
    DATABASE_URL,
    **DATABASE_PARAMS,
)
NewSession = sessionmaker(bind=engine)
