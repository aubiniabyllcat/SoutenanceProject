from dataclasses import dataclass

from fastapi import UploadFile

from image_service.interfaces.image_service_interface import ImageServiceInterface
from .interfaces.profile_repositories_interface import ProfileRepositoriesInterface
from .schemas import UpdateUserSchema


@dataclass
class ProfilePresenter:
    repositories: ProfileRepositoriesInterface

    # async def get_user(self, user_id: int):
    #     return await self.repositories.get_user(user_id=user_id)

    async def update_user(self, user_id: int, data: UpdateUserSchema):
        return await self.repositories.update_user(
            user_id=user_id, data=data)

    async def delete_user(self, user_id: int):
        return await self.repositories.delete_user(user_id=user_id)

    async def delete_image(
            self, image_name: str, user_id: int,
            image_service: ImageServiceInterface
    ):
        return await self.repositories.delete_image(
            image_name=image_name, user_id=user_id,
            image_service=image_service
        )

    async def add_images(self, images: list[UploadFile] | None, user_id: int,
                         file_service: ImageServiceInterface):
        await self.repositories \
            .update_profile_image(images=images, user_id=user_id,
                                  file_service=file_service)
