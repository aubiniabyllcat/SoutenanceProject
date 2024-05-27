from abc import ABC, abstractmethod
from ..schemas import CreateEnseignantSchema, UpdateEnseignantSchema


class EnseignantRepositoriesInterface(ABC):

    @abstractmethod
    async def get_enseignants(self, user_id: int, limit: int, offset: int):
        pass

    @abstractmethod
    async def create_enseignant(
            self, user_id: int, enseignant_data: CreateEnseignantSchema):
        pass

    @abstractmethod
    async def delete_enseignant(self, user_id: int, enseignant_slug: str):
        pass

    async def update_enseignant(
            self, user_id: int, enseignant_slug: str,
            updated_data: UpdateEnseignantSchema
    ):
        pass

    @abstractmethod
    async def get_enseignant(self, enseignant_slug: str):
        pass


    
    