from pydantic import BaseModel, Field


class BaseUserAccountSchema(BaseModel):
    username: str = Field(max_length=200)


class CreateUserSchema(BaseUserAccountSchema):
    password: str
    nom: str
    prenoms: str
    role_id: int


class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class ResetPasswordRequestSchema(BaseModel):
    username: str

class ResetPasswordConfirmSchema(BaseModel):
    token: str
    new_password: str