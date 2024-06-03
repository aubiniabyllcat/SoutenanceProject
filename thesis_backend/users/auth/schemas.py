from pydantic import BaseModel, Field


class BaseUserAccountSchema(BaseModel):
    username: str = Field(max_length=200)


class CreateUserSchema(BaseUserAccountSchema):
    password: str
    nom: str
    prenoms: str
    # matricule: str | None = Field(None, max_length=200)
    # specialite: str | None = Field(None, max_length=200)
    # departement_id: int | None 
    # annee_id: int | None
    # filiere_id: int | None
    # grade: str | None = Field(None, max_length=200)
    role_id: int



class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class ResetPasswordRequestSchema(BaseModel):
    username: str

class ResetPasswordConfirmSchema(BaseModel):
    token: str
    new_password: str