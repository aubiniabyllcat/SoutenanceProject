from pydantic import BaseModel, Field

from enseignants.schemas import CreateEnseignantSchema
from etudiants.schemas import CreateEtudiantSchema


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
    etudiant_data: CreateEtudiantSchema = None 
    enseignant_data: CreateEnseignantSchema = None 


class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class ResetPasswordRequestSchema(BaseModel):
    username: str

class ResetPasswordConfirmSchema(BaseModel):
    token: str
    new_password: str