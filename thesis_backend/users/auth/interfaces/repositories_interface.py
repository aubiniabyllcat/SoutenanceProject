from abc import ABC, abstractmethod


class UserRepositoriesInterface(ABC):

    @abstractmethod
    async def save_user(self, utilisateur_id: int, username: str, password: str, ): pass

    @abstractmethod
    async def receive_user_by_username(self, username: str): pass
