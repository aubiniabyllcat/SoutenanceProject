from pydantic import BaseModel, Field
from datetime import datetime

from users.profile.schemas import UserSchema


class CreateEcoleSchema(BaseModel):
    nom: str = Field(max_length=200)
    adresse: str = Field(max_length=200)
    directeur: str = Field(max_length=200)
    telephone: str = Field(max_length=200)
    email: str = Field(max_length=200)
    ville: str = Field(max_length=200)
    siteweb: str = Field(max_length=200)


class UpdateEcoleSchema(BaseModel):
    adresse: str | None = Field(None, max_length=200)
    directeur: str | None = Field(None, max_length=255)
    telephone: str | None = Field(None, max_length=200)
    email: str | None = Field(None, max_length=255)
    ville: str | None = Field(None, max_length=200)
    siteweb: str | None = Field(None, max_length=255)

    @property
    def is_empty(self): return not self.dict(exclude_none=True)


class EcoleSchema(CreateEcoleSchema):
    id: int
    slug: str | None
    created: datetime

    #online_users: list[UserSchema]
    #subscribers: list[UserSchema]

    class Config:
        orm_mode = True
