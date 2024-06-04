from dataclasses import dataclass
import logging
import traceback

from database import AsyncSessionLocal
from enseignants.interfaces.repositories_interface import EnseignantRepositoriesInterface
from enseignants.presenter import EnseignantPresenter
from enseignants.schemas import CreateEnseignantSchema
from etudiants.interfaces.repositories_interface import EtudiantRepositoriesInterface
from etudiants.presenter import EtudiantPresenter
from etudiants.schemas import CreateEtudiantSchema
from users.auth.repositories import UserRepositories
from .interfaces.repositories_interface import UserRepositoriesInterface
from .interfaces.password_service_interface import PasswordServiceInterface
from .interfaces.token_service_interface import TokenServiceInterface
from .interfaces.email_service_interface import EmailServiceInterface
from etudiants.repositories import EtudiantRepositories, EtudiantRepositories
from enseignants.repositories import EnseignantRepositories
from .exceptions import AuthExceptions
from .mixins import CreateTokenMixin
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import  AsyncSession




@dataclass
class TokenPresenter(CreateTokenMixin):
    token_service: TokenServiceInterface

    async def get_token(self, username: str) -> dict:
        return await self.create_token(
            username=username, token_service=self.token_service)

    
    
@dataclass
class UserPresenter(CreateTokenMixin):
    session: AsyncSession
    repository: UserRepositoriesInterface
    etudiant_repository: EtudiantRepositoriesInterface 
    enseignant_repository: EnseignantRepositoriesInterface 
    password_service: PasswordServiceInterface
    token_service: TokenServiceInterface
    email_service: EmailServiceInterface 

    async def __check(self, username: str, password: str):
        if not (user := await self.repository.receive_user_by_username(
                username=username)) or \
                not await self.password_service.verify_password(
                    plain_password=password,
                    hashed_password=user.password):
            raise AuthExceptions().incorrect_username_or_password
        return user

    async def login(self, username: str, password: str):
        user = await self.__check(username=username, password=password)
        return await self.create_token(
            username=user.username, token_service=self.token_service)

    async def sign_up(self, username: str, password: str, nom: str, prenoms: str, role_id: int, etudiant_data: CreateEtudiantSchema = None, enseignant_data: CreateEnseignantSchema = None):
        utilisateur_id = None
        try:
            # Vérifier si le nom d'utilisateur existe déjà
            if await self.repository.receive_user_by_username(username=username):
                raise AuthExceptions.username_exists
            
            # Hacher le mot de passe
            _password = await self.password_service.hashed_password(password=password)
            
            # Sauvegarder l'utilisateur et obtenir l'ID utilisateur
            utilisateur_id = await self.repository.save_user(username=username, password=_password, nom=nom, prenoms=prenoms, role_id=role_id)
            
            # Créer les données associées en fonction du rôle
            if etudiant_data and role_id == 1:  
                await self.etudiant_repository.create_etudiant(utilisateur_id=utilisateur_id, etudiant_data=etudiant_data)
            elif enseignant_data and role_id == 2:  # Rôle 'enseignant'
                await self.enseignant_repository.create_enseignant(utilisateur_id=utilisateur_id, enseignant_data=enseignant_data)
            
            # Valider la transaction
            await self.session.commit()
        
        except Exception as e:
            # Log de l'erreur et annulation de la transaction
            logging.error("Une erreur s'est produite lors de l'inscription : %s", e)
            logging.debug("Utilisateur ID: %s", utilisateur_id)
            logging.debug("Role ID: %s", role_id)
            logging.debug("Traceback: %s", traceback.format_exc())
            
            # Annuler la transaction en cas d'erreur
            await self.session.rollback()
            
            # Propager l'exception
            raise e
        else:
            # Commit the transaction if no error
            await self.session.commit()

    
        
    async def request_password_reset(self, username: str):
        user = await self.repository.receive_user_by_username(username=username)
        if not user:
            raise AuthExceptions().user_not_found
        
        reset_token = await self.token_service.create_reset_token(username=user.username)
        reset_link = f"https://yourdomain.com/reset-password?token={reset_token}"
        
        # Envoyer l'e-mail
        await self.email_service.send_password_reset_email(email=user.email, reset_link=reset_link)
        return {"message": "Password reset link sent"}

    async def reset_password(self, token: str, new_password: str):
        username = await self.verify_reset_token(token)
        _password = await self.password_service.hashed_password(password=new_password)
        await self.repository.update_password(username=username, new_password=_password)
        return {"message": "Password reset successful"}

    async def verify_reset_token(self, token: str):
        username = await self.token_service.verify_reset_token(token)
        if not username:
            raise AuthExceptions().invalid_or_expired_token
        return username