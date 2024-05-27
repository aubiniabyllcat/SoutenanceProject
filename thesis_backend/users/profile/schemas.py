from datetime import datetime
from fastapi import Form

from pydantic import BaseModel, Field


class UserImageSchema(BaseModel):
    id: int
    photo: str
    user_id: int

    class Config:
        orm_mode = True


class UpdateUserSchema(BaseModel):
    bio: str | None = Field(max_length=255)
    username: str | None = Field(max_length=200)
    

    @classmethod
    def as_form(
            cls, bio: str | None = Form(None),
            username: str | None = Form(None)
    ):
        return cls(bio=bio, username=username)


class UserSchema(UpdateUserSchema):
    id: int
    created: datetime
    is_active: bool = Field(True)
    images: list[UserImageSchema]

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda d: d.strftime('%Y-%m-%d %H:%M')
        }
