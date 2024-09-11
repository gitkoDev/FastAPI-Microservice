from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "notesdb"
DB_NAME = "postgres"

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

# engine = create_engine(DB_URL)
engine = create_async_engine(DB_URL)

# SessionLocal = sessionmaker(engine, autoflush=False, autocommit=False)
SessionLocal = async_sessionmaker(bind=engine, autoflush=False)
