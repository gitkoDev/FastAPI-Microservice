from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import dotenv_values

# get .env variables
config = dotenv_values()

# start sql engine
engine = create_async_engine(config["DB_URL"])

SessionLocal = async_sessionmaker(bind=engine, autoflush=False)
