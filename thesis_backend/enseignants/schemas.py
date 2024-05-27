from pydantic import BaseModel, Field
from datetime import datetime

from users.profile.schemas import UserSchema


class CreateEnseignantSchema(BaseModel):
    matricule: str = Field(max_length=200)
    grade: str
    specialite: str
    filiere_id: int 
    annee_id: int


class UpdateEnseignantSchema(BaseModel):
    matricule: str | None = Field(None, max_length=200)
    filiere: str | None = Field(None, max_length=255)

    @property
    def is_empty(self): return not self.dict(exclude_none=True)


class EnseignantSchema(CreateEnseignantSchema):
    id: int
    user_id: int
    slug: str | None
    created: datetime

    #online_users: list[UserSchema]
    #subscribers: list[UserSchema]

    class Config:
        orm_mode = True
