from fastapi import APIRouter, Depends

from typing import Annotated

from repository import UserRepository
from schemas.user import UserSchema, UserAddSchema
from models.user import UserModel

router = APIRouter(prefix="/users")


@router.post("")
async def add_user(user: Annotated[UserAddSchema, Depends()]):
    user = UserRepository.add_user(user)
    return {"okay": user}


@router.get("", response_model=list[UserSchema])
async def get_users():
    users = UserRepository.get_users()
    return users
