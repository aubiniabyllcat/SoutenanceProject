from dataclasses import dataclass
from .schemas import UpdateEnseignantSchema, CreateEnseignantSchema
from .interfaces.repositories_interface import \
    EnseignantRepositoriesInterface
from .exceptions import EnseignantExceptions


@dataclass
class EnseignantPresenter:
    repository: EnseignantRepositoriesInterface

    async def get_enseignants(self, user_id: int, limit: int, offset: int):
        data = {'user_id': user_id, 'limit': limit, 'offset': offset}
        return await self.repository.get_enseignants(**data)


    async def create_enseignant(
            self, user_id: int, enseignant_data: CreateEnseignantSchema):
        data = {'user_id': user_id, 'enseignant_data': enseignant_data}
        return await self.repository.create_enseignant(**data)

    async def delete_enseignant(self, user_id: int, enseignant_slug: str):
        data = {'user_id': user_id, 'enseignant_slug': enseignant_slug}
        if not await self.repository.delete_enseignant(**data):
            raise EnseignantExceptions().enseignant_not_found
        
    async def update_enseignant(
            self, user_id: int, enseignant_slug: str,
            updated_data: UpdateEnseignantSchema
    ):
        if updated_data.is_empty:
            raise EnseignantExceptions().empty_data
        return await self.repository \
            .update_enseignant(user_id=user_id, enseignant_slug=enseignant_slug,
                            updated_data=updated_data)
    
    async def get_enseignant(self, enseignant_slug: str):
        data = {'enseignant_slug': enseignant_slug}
        if (result := await self.repository.get_enseignant(**data)) is None:
            raise EnseignantExceptions().enseignant_not_found
        return result