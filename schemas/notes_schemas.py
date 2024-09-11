from pydantic import BaseModel, ConfigDict

from datetime import datetime


class NoteInput(BaseModel):
    content: str
    user_id: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class NoteOutput(NoteInput):
    id: int

    model_config = ConfigDict(from_attributes=True)
