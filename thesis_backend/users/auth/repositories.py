from .interfaces.repositories_interface import UserRepositoriesInterface
from etudiants.interfaces.repositories_interface import EtudiantRepositoriesInterface
from enseignants.interfaces.repositories_interface import EnseignantRepositoriesInterface
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from .models import Users


@dataclass
class UserRepositories(UserRepositoriesInterface):
    session: AsyncSession

    async def save_user(self, username: str, password: str, nom: str, prenoms: str, role_id: int) -> int:
        stmt = insert(Users).values(
            username=username,
            password=password,
            nom=nom,
            prenoms=prenoms,
            role_id=role_id
        ).returning(Users.id)
        result = await self.session.execute(statement=stmt)
        await self.session.commit()
        utilisateur_id = result.scalar_one()
        return utilisateur_id


    async def receive_user_by_username(self, username: str):
        stmt = select(Users).where(Users.username == username)
        result = await self.session.execute(statement=stmt)
        return result.scalars().first()
    
    