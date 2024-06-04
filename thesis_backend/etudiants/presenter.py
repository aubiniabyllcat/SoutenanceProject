from dataclasses import dataclass
from .schemas import UpdateEtudiantSchema, CreateEtudiantSchema
from .interfaces.repositories_interface import \
    EtudiantRepositoriesInterface
from .exceptions import EtudiantExceptions


@dataclass
class EtudiantPresenter:
    repository: EtudiantRepositoriesInterface

    async def get_etudiants(self, limit: int, offset: int):
        data = { 'limit': limit, 'offset': offset}
        return await self.repository.get_etudiants(**data)


    async def create_etudiant(
            self, etudiant_data: CreateEtudiantSchema):
        data = { 'etudiant_data': etudiant_data}
        return await self.repository.create_etudiant(**data)

    async def delete_etudiant(self, utilisateur_id: int, etudiant_slug: str):
        data = {'utilisateur_id': utilisateur_id, 'etudiant_slug': etudiant_slug}
        if not await self.repository.delete_etudiant(**data):
            raise EtudiantExceptions().etudiant_not_found
        
    async def update_etudiant(
            self, utilisateur_id: int, etudiant_slug: str,
            updated_data: UpdateEtudiantSchema
    ):
        if updated_data.is_empty:
            raise EtudiantExceptions().empty_data
        return await self.repository \
            .update_etudiant(utilisateur_id=utilisateur_id, etudiant_slug=etudiant_slug,
                            updated_data=updated_data)
    
    async def get_etudiant(self, etudiant_slug: str):
        data = {'etudiant_slug': etudiant_slug}
        if (result := await self.repository.get_etudiant(**data)) is None:
            raise EtudiantExceptions().etudiant_not_found
        return result