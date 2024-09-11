from fastapi import FastAPI

from router.note_routes import router as notes_router
from router.auth_routes import router as auth_router


app = FastAPI(title="Notes Service", version="1.0")
app.include_router(auth_router)
app.include_router(notes_router)
