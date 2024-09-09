from pydantic import BaseModel, ConfigDict


class UserAddSchema(BaseModel):
    name: str


class UserSchema(UserAddSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)
