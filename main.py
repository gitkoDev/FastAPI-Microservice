from fastapi import FastAPI
from dotenv import load_dotenv

from api.router.note_routes import router as notes_router
from api.router.auth_routes import router as auth_router

# app config
load_dotenv()

# app startup
app = FastAPI(title="Notes Service", version="1.0")
app.include_router(auth_router)
app.include_router(notes_router)
