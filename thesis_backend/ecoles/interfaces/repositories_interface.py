from abc import ABC, abstractmethod
from ..schemas import CreateEcoleSchema, UpdateEcoleSchema


class EcoleRepositoriesInterface(ABC):

    @abstractmethod
    async def get_ecoles(self, utilisateur_id: int, limit: int, offset: int):
        pass

    @abstractmethod
    async def create_ecole(
            self, utilisateur_id: int, ecole_data: CreateEcoleSchema):
        pass

    @abstractmethod
    async def delete_ecole(self, utilisateur_id: int, ecole_slug: str):
        pass

    async def update_ecole(
            self, utilisateur_id: int, ecole_slug: str,
            updated_data: UpdateEcoleSchema
    ):
        pass

    @abstractmethod
    async def get_ecole(self, ecole_slug: str):
        pass


    
    