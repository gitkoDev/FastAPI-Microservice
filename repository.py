from sqlalchemy import select
from models.user import UserModel
from schemas.user import UserSchema, UserAddSchema
from database.database import new_session


class UserRepository:
    @classmethod
    def add_user(cls, data: UserAddSchema) -> int:
        with new_session() as session:
            user_dict = data.model_dump()
            user = UserModel(**user_dict)

            session.add(user)
            session.flush()
            session.commit()
            return user.id

    @classmethod
    def get_users(cls) -> list[UserSchema]:
        with new_session() as session:
            query = select(UserModel)
            result = session.execute(query)
            user_models = result.scalars().all()
            user_schemas = [
                UserSchema.model_validate(user_model) for user_model in user_models
            ]
            return user_schemas
