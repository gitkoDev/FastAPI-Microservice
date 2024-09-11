from fastapi import Depends
from jose import jwt, JWTError
from sqlalchemy.future import select

from datetime import datetime, timedelta
from typing import Annotated

from models.user_models import UserModel
from schemas.user_schemas import (
    CreateUserInput,
    bcrypt_context,
    SECRET_KEY,
    ALGORITHM,
    oauth2_bearer,
)
from config.database import SessionLocal


class AuthRepository:
    @classmethod
    async def create_user(cls, data: CreateUserInput) -> int:
        async with SessionLocal() as session:
            user = UserModel(
                name=data.name, password_hash=bcrypt_context.hash(data.password)
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user.id

    @classmethod
    async def authenticate_user(cls, name: str, password: str):
        async with SessionLocal() as session:
            query = select(UserModel).where(UserModel.name == name)
            result = await session.execute(query)
            user = result.scalars().one()
            if not user:
                return False
            if not bcrypt_context.verify(password, user.password_hash):
                return False
            return user

    @classmethod
    def create_access_token(cls, name: str, id: int, ttl: timedelta):
        data_to_encode = {"sub": name, "id": id}
        expires = datetime.now() + ttl
        data_to_encode.update({"exp": expires})
        return jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @classmethod
    def parse_access_token(cls, token: Annotated[str, Depends(oauth2_bearer)]):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            user_id: str = payload.get("id")
            if username is None or user_id is None:
                return False
            return {"username": username, "user_id": user_id}
        except JWTError:
            return False
