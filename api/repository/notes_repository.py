from sqlalchemy.future import select

from config.database import SessionLocal
from api.schemas.notes_schemas import NoteOutput, NoteInput
from api.models.notes_models import NoteModel
from helpers.helpers import NotFoundError


class NotesRepository:
    @classmethod
    async def add_note(cls, data: NoteInput, user_id: int) -> int:
        async with SessionLocal() as session:
            note_dict = data.model_dump()
            note = NoteModel(**note_dict)
            note.user_id = user_id
            session.add(note)
            await session.commit()
            await session.refresh(note)
            return note.id

    @classmethod
    async def get_notes(cls, user_id: int) -> list[NoteOutput]:
        async with SessionLocal() as session:
            query = select(NoteModel).where(NoteModel.user_id == user_id)
            result = await session.execute(query)
            note_models = result.scalars().all()
            notes_schemas = [
                NoteOutput.model_validate(note_model) for note_model in note_models
            ]
            return notes_schemas

    @classmethod
    async def get_note(cls, note_id: int, user_id: int) -> NoteOutput:
        async with SessionLocal() as session:
            query = select(NoteModel).where(
                NoteModel.id == note_id, NoteModel.user_id == user_id
            )
            result = await session.execute(query)
            note_model = result.scalars().one_or_none()
            if not note_model:
                raise NotFoundError
            note = NoteOutput.model_validate(note_model)
            return note

    @classmethod
    async def update_note(
        cls, note_id: int, data: NoteInput, user_id: int
    ) -> NoteOutput:
        async with SessionLocal() as session:
            query = select(NoteModel).where(
                NoteModel.id == note_id, NoteModel.user_id == user_id
            )
            result = await session.execute(query)
            note_model = result.scalars().one_or_none()
            if not note_model:
                raise NotFoundError

            note_model.content = data.content

            await session.commit()
            await session.refresh(note_model)

            note = NoteOutput.model_validate(note_model)
            return note

    @classmethod
    async def delete_note(cls, note_id: int, user_id: int):
        async with SessionLocal() as session:
            query = select(NoteModel).where(
                NoteModel.id == note_id, NoteModel.user_id == user_id
            )
            result = await session.execute(query)
            note_model = result.scalars().one_or_none()
            if not note_model:
                raise NotFoundError

            await session.delete(note_model)
            await session.commit()
