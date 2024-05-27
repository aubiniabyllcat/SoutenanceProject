from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import subqueryload
from .schemas import CreateEnseignantSchema, UpdateEnseignantSchema
from .models import Enseignant
from .exceptions import EnseignantExceptions
from .interfaces.repositories_interface import \
    EnseignantRepositoriesInterface


@dataclass
class EnseignantRepositories(EnseignantRepositoriesInterface):
    session: AsyncSession


    async def get_enseignants(self, user_id: int, limit: int, offset: int):
        stmt = select(Enseignant) \
        .order_by(Enseignant.created.desc()) \
        .limit(limit) \
        .offset(offset)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def create_enseignant(
            self, user_id: int, enseignant_data: CreateEnseignantSchema):
        values = {
            'user_id': user_id,
            'slug': enseignant_data.matricule,
            **enseignant_data.dict(exclude_none=True)
        }
        stmt = insert(Enseignant).values(**values).returning(Enseignant)
        result = await self.session.execute(statement=stmt)
        await self.session.commit()
        return result.first()
    
    async def delete_enseignant(self, user_id: int, enseignant_slug: str):
        cond = (Enseignant.user_id == user_id, Enseignant.slug == enseignant_slug)
        stmt = delete(Enseignant).where(*cond)
        result = await self.session.execute(statement=stmt)
        await self.session.commit()
        return result.rowcount

    async def update_enseignant(
            self, user_id: int, enseignant_slug: str,
            updated_data: UpdateEnseignantSchema
    ):
        await self.__check_enseignant(enseignant_slug=enseignant_slug)
        values = {**updated_data.dict(exclude_none=True)}
        if updated_data.matricule:
            values.update({'slug': updated_data.matricule})
        cond = (Enseignant.slug == enseignant_slug, Enseignant.user_id == user_id)
        stmt = update(Enseignant).where(*cond).values(**values)
        await self.session.execute(statement=stmt)
        await self.session.commit()

    
    async def get_enseignant(self, enseignant_slug: str):
        stmt = select(Enseignant) \
            .where(Enseignant.slug == enseignant_slug)
        result: AsyncResult = await self.session.execute(statement=stmt)
        return result.scalars().first()

    
    async def __check_enseignant(self, enseignant_slug: str):
        if not (enseignant := await self.get_enseignant(enseignant_slug=enseignant_slug)):
            raise EnseignantExceptions().enseignant_not_found
        return enseignant
