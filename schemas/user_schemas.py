from pydantic import BaseModel, ConfigDict
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = "fj549fgjkkccxcmk7677kksals4"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


class CreateUserInput(BaseModel):
    name: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
