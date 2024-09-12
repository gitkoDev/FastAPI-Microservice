from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from typing import Annotated

from api.schemas.notes_schemas import NoteInput, NoteOutput
from api.repository.notes_repository import NotesRepository
from api.repository.auth_repository import AuthRepository
from helpers.helpers import NotFoundError


router = APIRouter(
    prefix="/api/v1",
    tags=["Notes"],
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_note(
    user: Annotated[dict, Depends(AuthRepository.parse_access_token)],
    data: NoteInput,
) -> dict:
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )
    note_id = await NotesRepository.add_note(data, user.get("user_id"))
    return {"okay": note_id}


@router.get("", response_model=list[NoteOutput])
async def get_notes(
    user: Annotated[dict, Depends(AuthRepository.parse_access_token)]
) -> list[NoteOutput]:
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )
    notes = await NotesRepository.get_notes(user.get("user_id"))
    return notes


@router.get("/{note_id}", response_model=NoteOutput)
async def get_note(
    user: Annotated[dict, Depends(AuthRepository.parse_access_token)], note_id: int
) -> NoteOutput:
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )
    try:
        note = await NotesRepository.get_note(note_id, user.get("user_id"))
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found",
        )
    return note


@router.put("/{note_id}", response_model=NoteOutput)
async def update_note(
    user: Annotated[dict, Depends(AuthRepository.parse_access_token)],
    note_id: int,
    data: NoteInput,
) -> NoteOutput:
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )
    try:
        note = await NotesRepository.update_note(note_id, data, user.get("user_id"))
    except NotFoundError:
        raise HTTPException(status_code=404, detail=f"Note with id {note_id} not found")
    return note


@router.delete("/{note_id}")
async def delete_note(
    user: Annotated[dict, Depends(AuthRepository.parse_access_token)], note_id: int
) -> dict:
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )
    try:
        await NotesRepository.delete_note(note_id, user.get("user_id"))
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found",
        )
    return {"okay": note_id}
