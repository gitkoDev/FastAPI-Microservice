from pydantic import BaseModel, ConfigDict

from datetime import datetime


class NoteInput(BaseModel):
    content: str


class NoteOutput(NoteInput):
    id: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    model_config = ConfigDict(from_attributes=True)
