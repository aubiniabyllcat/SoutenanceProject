from fastapi import status, Depends
from permissions import UserPermission
from users.auth.token_service import TokenService
from .schemas import EtudiantSchema, CreateEtudiantSchema, UpdateEtudiantSchema
from .repositories import EtudiantRepositories

from .presenter import EtudiantPresenter
from database import get_db_session


async def get_user(
        user=Depends(UserPermission(token_service=TokenService())
                         .get_current_user)
):
    yield user


# async def get_repository_service(session=Depends(get_db_session)):
#     yield {
#         'repository': ChannelRepositories(session=session)
#     }


async def get_presenter(session=Depends(get_db_session)):
    presenter = EtudiantPresenter(
        repository=EtudiantRepositories(session=session))
    yield presenter


async def get_etudiant_user(etudiant_id: int) -> dict:
    return {'etudiant_id': etudiant_id}


async def get_limit_offset_user( limit: int, offset: int) -> dict:
    return { 'limit': limit, 'offset': offset}


async def get_slug_user(etudiant_slug: str) -> dict:
    return {'etudiant_slug': etudiant_slug}


async def get_updated_data_slug_user(updated_data: UpdateEtudiantSchema,
                                         etudiant_slug: str,
                                         ) -> dict:
    return {
        'updated_data': updated_data,
        'etudiant_slug': etudiant_slug,
        
    }


async def get_create_data_user(
                                   etudiant_data: CreateEtudiantSchema) -> dict:
    return { 'etudiant_data': etudiant_data}


response_data = {
    
    'etudiants': {
        'path': '/',
        'status_code': status.HTTP_200_OK,
        # 'response_model': list[ChannelSchema]
    },
    'create_etudiants': {
        'path': '/',
        'status_code': status.HTTP_201_CREATED,
    },
    'delete_etudiants': {
        'path': '/{matricule}',
        'status_code': status.HTTP_204_NO_CONTENT,
    },
    'update_etudiant': {
        'path': '/{matricule}',
        'status_code': status.HTTP_200_OK,
    },
   'etudiant': {
        'path': '/{matricule}',
        'status_code': status.HTTP_200_OK,
        'response_model': EtudiantSchema
    },
}
