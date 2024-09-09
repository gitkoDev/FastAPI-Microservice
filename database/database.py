from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://postgres:1234@localhost:5432/postgres"

engine = create_engine(DB_URL)

new_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
