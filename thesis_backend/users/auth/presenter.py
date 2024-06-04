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

    async def sign_up(
            self, 
            username: str, 
            password: str, 
            nom: str, 
            prenoms: str, 
            role_id: int, 
            matricule: str, 
            specialite: str,
            departement_id: int, 
            annee_id: int, 
            grade: str, 
            filiere_id: int,):
        
        async with AsyncSessionLocal() as session:
            try:
                async with session.begin():
                    # Vérifier si l'utilisateur existe déjà
                    if await self.repository.receive_user_by_username(username=username):
                        raise AuthExceptions().username_exists
                    
                    # Hacher le mot de passe
                    _password = await self.password_service.hashed_password(password=password)
                    
                    # Enregistrer l'utilisateur et récupérer l'utilisateur_id
                    utilisateur_id = await self.repository.save_user(
                        username=username,
                        password=_password,
                        nom=nom,
                        prenoms=prenoms,
                        role_id=role_id)
                    
                    print(f"User {username} saved successfully. Utilisateur ID: {utilisateur_id} role: {role_id}")
                    utilisateur_id=utilisateur_id
                    print(utilisateur_id)

                    # En fonction du role_id, insérer les données supplémentaires dans la table correspondante
                    if role_id == 1:  # Etudiant
                        etudiant_data = CreateEtudiantSchema(
                            matricule=matricule,
                            annee_id=annee_id,
                            filiere_id=filiere_id,
                            utilisateur_id=utilisateur_id
                            )
                        
                        etudiant = await self.etudiant_repository.create_etudiant(etudiant_data=etudiant_data)
                        return etudiant
                        print(f"Etudiant created successfully for user {username}.")
                    elif role_id == 2:  # Enseignant
                        enseignant_data = CreateEnseignantSchema(
                            matricule=matricule,
                            specialite=specialite,
                            grade=grade,
                            departement_id=departement_id,
                            utilisateur_id=utilisateur_id
                            )
                        
                        await self.enseignant_repository.create_enseignant(enseignant_data=enseignant_data)
                        print(f"Enseignant created successfully for user {username}.")
                    else:
                        raise ValueError("Invalid role_id")
                
            except Exception as e:
                print("Il y a erreur:", e)
                await session.rollback()
                raise e

        
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