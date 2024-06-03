from abc import ABC, abstractmethod
from ..schemas import CreateEtudiantSchema, UpdateEtudiantSchema


class EtudiantRepositoriesInterface(ABC):

    @abstractmethod
    async def get_etudiants(self, utilisateur_id: int, limit: int, offset: int):
        pass

    @abstractmethod
    async def create_etudiant(
            self, utilisateur_id: int, etudiant_data: CreateEtudiantSchema):
        pass

    @abstractmethod
    async def delete_etudiant(self, utilisateur_id: int, etudiant_slug: str):
        pass

    async def update_etudiant(
            self, utilisateur_id: int, etudiant_slug: str,
            updated_data: UpdateEtudiantSchema
    ):
        pass

    @abstractmethod
    async def get_etudiant(self, etudiant_slug: str):
        pass


    
    