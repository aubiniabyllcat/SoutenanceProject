from dataclasses import dataclass
from .schemas import UpdateEcoleSchema, CreateEcoleSchema
from .interfaces.repositories_interface import \
    EcoleRepositoriesInterface
from .exceptions import EcoleExceptions


@dataclass
class EcolePresenter:
    repository: EcoleRepositoriesInterface

    async def get_ecoles(self, utilisateur_id: int, limit: int, offset: int):
        data = {'utilisateur_id': utilisateur_id, 'limit': limit, 'offset': offset}
        return await self.repository.get_ecoles(**data)


    async def create_ecole(
            self, utilisateur_id: int, ecole_data: CreateEcoleSchema):
        data = {'utilisateur_id': utilisateur_id, 'etudiant_data': ecole_data}
        return await self.repository.create_ecole(**data)

    async def delete_ecole(self, utilisateur_id: int, ecole_slug: str):
        data = {'utilisateur_id': utilisateur_id, 'ecole_slug': ecole_slug}
        if not await self.repository.delete_ecole(**data):
            raise EcoleExceptions().ecole_not_found
        
    async def update_ecole(
            self, utilisateur_id: int, ecole_slug: str,
            updated_data: UpdateEcoleSchema
    ):
        if updated_data.is_empty:
            raise EcoleExceptions().empty_data
        return await self.repository \
            .update_ecole(utilisateur_id=utilisateur_id, ecole_slug=ecole_slug,
                            updated_data=updated_data)
    
    async def get_ecole(self, ecole_slug: str):
        data = {'ecole_slug': ecole_slug}
        if (result := await self.repository.get_ecole(**data)) is None:
            raise EcoleExceptions().ecole_not_found
        return result