from fastapi import status, Depends
from permissions import UserPermission
from users.auth.token_service import TokenService
from .schemas import EcoleSchema, CreateEcoleSchema, UpdateEcoleSchema
from .repositories import EcoleRepositories

from .presenter import EcolePresenter
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
    presenter = EcolePresenter(
        repository=EcoleRepositories(session=session))
    yield presenter


async def get_ecole_user(ecole_id: int, utilisateur_id: int) -> dict:
    return {'ecole_id': ecole_id, 'utilisateur_id': utilisateur_id}


async def get_limit_offset_user(utilisateur_id: int, limit: int, offset: int) -> dict:
    return {'utilisateur_id': utilisateur_id, 'limit': limit, 'offset': offset}


async def get_slug_user(ecole_slug: str, utilisateur_id: int) -> dict:
    return {'ecole_slug': ecole_slug, 'utilisateur_id': utilisateur_id}


async def get_updated_data_slug_user(updated_data: UpdateEcoleSchema,
                                         ecole_slug: str,
                                         utilisateur_id: int) -> dict:
    return {
        'updated_data': updated_data,
        'ecole_slug': ecole_slug,
        'utilisateur_id': utilisateur_id
    }


async def get_create_data_user(utilisateur_id: int,
                                   ecole_data: CreateEcoleSchema) -> dict:
    return {'utilisateur_id': utilisateur_id, 'ecole_data': ecole_data}


response_data = {
    
    'ecoles': {
        'path': '/',
        'status_code': status.HTTP_200_OK,
        # 'response_model': list[ChannelSchema]
    },
    'create_ecoles': {
        'path': '/',
        'status_code': status.HTTP_201_CREATED,
    },
    'delete_ecoles': {
        'path': '/{nom}',
        'status_code': status.HTTP_204_NO_CONTENT,
    },
    'update_ecole': {
        'path': '/{nom}',
        'status_code': status.HTTP_200_OK,
    },
   'ecole': {
        'path': '/{nom}',
        'status_code': status.HTTP_200_OK,
        'response_model': EcoleSchema
    },
}
