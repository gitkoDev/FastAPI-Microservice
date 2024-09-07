from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str]
    completed: bool = False
