from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import subqueryload
from .schemas import CreateEcoleSchema, UpdateEcoleSchema
from .models import Ecole
from .exceptions import EcoleExceptions
from .interfaces.repositories_interface import \
    EcoleRepositoriesInterface


@dataclass
class EcoleRepositories(EcoleRepositoriesInterface):
    session: AsyncSession
    

    async def get_ecoles(self, utilisateur_id: int, limit: int, offset: int):
        stmt = select(Ecole) \
        .order_by(Ecole.created.desc()) \
        .limit(limit) \
        .offset(offset)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def create_ecole(
            self, utilisateur_id: int, ecole_data: CreateEcoleSchema):
        values = {
            'utilisateur_id': utilisateur_id,
            'slug': ecole_data.nom,
            **ecole_data.dict(exclude_none=True)
        }
        stmt = insert(Ecole).values(**values).returning(Ecole)
        result = await self.session.execute(statement=stmt)
        await self.session.commit()
        return result.first()
    
    async def delete_ecole(self, utilisateur_id: int, ecole_slug: str):
        cond = (Ecole.utilisateur_id == utilisateur_id, Ecole.slug == ecole_slug)
        stmt = delete(Ecole).where(*cond)
        result = await self.session.execute(statement=stmt)
        await self.session.commit()
        return result.rowcount

    async def update_ecole(
            self, utilisateur_id: int, ecole_slug: str,
            updated_data: UpdateEcoleSchema
    ):
        await self.__check_ecole(ecole_slug=ecole_slug)
        values = {**updated_data.dict(exclude_none=True)}
        if updated_data.nom:
            values.update({'slug': updated_data.nom})
        cond = (Ecole.slug == ecole_slug, Ecole.utilisateur_id == utilisateur_id)
        stmt = update(Ecole).where(*cond).values(**values)
        await self.session.execute(statement=stmt)
        await self.session.commit()

    
    async def get_ecole(self, ecole_slug: str):
        stmt = select(Ecole) \
            .where(Ecole.slug == ecole_slug)
        result: AsyncResult = await self.session.execute(statement=stmt)
        return result.scalars().first()

    
    async def __check_ecole(self, ecole_slug: str):
        if not (ecole := await self.get_ecole(ecole_slug=ecole_slug)):
            raise EcoleExceptions().ecole_not_found
        return ecole
