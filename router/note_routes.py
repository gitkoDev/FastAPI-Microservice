from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from typing import Annotated

from schemas.notes_schemas import NoteInput, NoteOutput
from schemas.user_schemas import oauth2_bearer
from repository.notes_repository import NotesRepository
from repository.auth_repository import AuthRepository
from helpers.helpers import NotFoundError


router = APIRouter(
    prefix="/api/v1",
    tags=["Notes"],
    dependencies=[Depends(oauth2_bearer)],
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_note(data: Annotated[NoteInput, Depends()]):
    note_id = await NotesRepository.add_note(data)
    return {"okay": note_id}


@router.get("", response_model=list[NoteOutput])
async def get_notes():
    notes = await NotesRepository.get_notes()
    return notes


@router.get("/{note_id}", response_model=NoteOutput)
async def get_note(note_id: int):
    try:
        note = await NotesRepository.get_note(note_id)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found",
        )
    return note


@router.put("/{note_id}", response_model=NoteOutput)
async def update_note(note_id: int, data: Annotated[NoteInput, Depends()]):
    try:
        note = await NotesRepository.update_note(note_id, data)
    except NotFoundError:
        raise HTTPException(status_code=404, detail=f"Note with id {note_id} not found")
    return note


@router.delete("/{note_id}")
async def delete_note(note_id: int):
    try:
        await NotesRepository.delete_note(note_id)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found",
        )
    return {"okay": note_id}
