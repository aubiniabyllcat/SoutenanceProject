from fastapi import status, Depends
from permissions import UserPermission
from users.auth.token_service import TokenService
from .schemas import EnseignantSchema, CreateEnseignantSchema, UpdateEnseignantSchema
from .repositories import EnseignantRepositories

from .presenter import EnseignantPresenter
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
    presenter = EnseignantPresenter(
        repository=EnseignantRepositories(session=session))
    yield presenter


async def get_enseignant_user(enseignant_id: int, user_id: int) -> dict:
    return {'enseignant_id': enseignant_id, 'user_id': user_id}


async def get_limit_offset_user(user_id: int, limit: int, offset: int) -> dict:
    return {'user_id': user_id, 'limit': limit, 'offset': offset}


async def get_slug_user(enseignant_slug: str, user_id: int) -> dict:
    return {'enseignant_slug': enseignant_slug, 'user_id': user_id}


async def get_updated_data_slug_user(updated_data: UpdateEnseignantSchema,
                                         enseignant_slug: str,
                                         user_id: int) -> dict:
    return {
        'updated_data': updated_data,
        'enseignant_slug': enseignant_slug,
        'user_id': user_id
    }


async def get_create_data_user(user_id: int,
                                   enseignant_data: CreateEnseignantSchema) -> dict:
    return {'user_id': user_id, 'enseignant_data': enseignant_data}


response_data = {
    
    'enseignants': {
        'path': '/',
        'status_code': status.HTTP_200_OK,
        # 'response_model': list[ChannelSchema]
    },
    'create_enseignants': {
        'path': '/',
        'status_code': status.HTTP_201_CREATED,
    },
    'delete_enseignants': {
        'path': '/{matricule}',
        'status_code': status.HTTP_204_NO_CONTENT,
    },
    'update_enseignant': {
        'path': '/{matricule}',
        'status_code': status.HTTP_200_OK,
    },
   'enseignant': {
        'path': '/{matricule}',
        'status_code': status.HTTP_200_OK,
        'response_model': EnseignantSchema
    },
}
