from .interfaces.repositories_interface import UserRepositoriesInterface
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from .models import Users


@dataclass
class UserRepositories(UserRepositoriesInterface):
    session: AsyncSession

    async def save_user(self, username: str, password: str, nom: str, prenoms: str, role_id: int):
    # Implémentez ici la logique pour enregistrer l'utilisateur avec les nouveaux champs

        stmt = insert(Users).values(username=username, password=password, nom=nom, prenoms=prenoms, role_id=role_id)
        _ = await self.session.execute(statement=stmt)
        await self.session.commit()

    async def receive_user_by_username(self, username: str):
        stmt = select(Users).where(Users.username == username)
        result = await self.session.execute(statement=stmt)
        return result.scalars().first()
