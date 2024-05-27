from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import subqueryload
from .schemas import CreateEtudiantSchema, UpdateEtudiantSchema
from .models import Etudiant
from .exceptions import EtudiantExceptions
from .interfaces.repositories_interface import \
    EtudiantRepositoriesInterface


@dataclass
class EtudiantRepositories(EtudiantRepositoriesInterface):
    session: AsyncSession


    async def get_etudiants(self, user_id: int, limit: int, offset: int):
        stmt = select(Etudiant) \
        .order_by(Etudiant.created.desc()) \
        .limit(limit) \
        .offset(offset)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def create_etudiant(
            self, user_id: int, etudiant_data: CreateEtudiantSchema):
        values = {
            'user_id': user_id,
            'slug': etudiant_data.matricule,
            **etudiant_data.dict(exclude_none=True)
        }
        stmt = insert(Etudiant).values(**values).returning(Etudiant)
        result = await self.session.execute(statement=stmt)
        await self.session.commit()
        return result.first()
    
    async def delete_etudiant(self, user_id: int, etudiant_slug: str):
        cond = (Etudiant.user_id == user_id, Etudiant.slug == etudiant_slug)
        stmt = delete(Etudiant).where(*cond)
        result = await self.session.execute(statement=stmt)
        await self.session.commit()
        return result.rowcount

    async def update_etudiant(
            self, user_id: int, etudiant_slug: str,
            updated_data: UpdateEtudiantSchema
    ):
        await self.__check_etudiant(etudiant_slug=etudiant_slug)
        values = {**updated_data.dict(exclude_none=True)}
        if updated_data.matricule:
            values.update({'slug': updated_data.matricule})
        cond = (Etudiant.slug == etudiant_slug, Etudiant.user_id == user_id)
        stmt = update(Etudiant).where(*cond).values(**values)
        await self.session.execute(statement=stmt)
        await self.session.commit()

    
    async def get_etudiant(self, etudiant_slug: str):
        stmt = select(Etudiant) \
            .where(Etudiant.slug == etudiant_slug)
        result: AsyncResult = await self.session.execute(statement=stmt)
        return result.scalars().first()

    
    async def __check_etudiant(self, etudiant_slug: str):
        if not (etudiant := await self.get_etudiant(etudiant_slug=etudiant_slug)):
            raise EtudiantExceptions().etudiant_not_found
        return etudiant
