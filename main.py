from fastapi import FastAPI
from sqlalchemy.orm import session

from database.database import engine, new_session
from routers.routes import router


app = FastAPI(title="Trading App", version="1.0")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
