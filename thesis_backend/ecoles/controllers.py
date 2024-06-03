from fastapi import APIRouter, Depends
from .presenter import EcolePresenter
from .schemas import CreateEcoleSchema, UpdateEcoleSchema
from .deps import response_data, get_user, get_presenter, \
   get_slug_user, get_updated_data_slug_user, get_limit_offset_user,  \
    get_create_data_user

ecole_controllers = APIRouter(prefix='/ecoles', tags=['ecoles'])


@ecole_controllers.get(**response_data.get('ecoles'))
async def get_ecoles(
        user=Depends(get_user),
        presenter: EcolePresenter = Depends(get_presenter),
        limit: int | None = 20, offset: int | None = 0
):
    data: dict = await get_limit_offset_user(user.id, limit, offset)
    return await presenter.get_ecoles(**data)

@ecole_controllers.post(**response_data.get('create_ecoles'))
async def create_ecole(
        ecole_data: CreateEcoleSchema,
        presenter: EcolePresenter = Depends(get_presenter),
):
    data: dict = await get_create_data_user( ecole_data)
    return await presenter.create_ecole(**data)

@ecole_controllers.delete(**response_data.get('delete_ecoles'))
async def delete_ecole(
        nom: str, user=Depends(get_user),
        presenter: EcolePresenter = Depends(get_presenter),
):
    data: dict = await get_slug_user(nom, user.id)
    return await presenter.delete_ecole(**data)

@ecole_controllers.patch(**response_data.get('update_ecole'))
async def update_ecole(
        updated_data: UpdateEcoleSchema,
        nom: str, user=Depends(get_user),
        presenter: EcolePresenter = Depends(get_presenter),
):
    data: dict = await get_updated_data_slug_user(
        updated_data, nom, user.id)
    return await presenter.update_etudiant(**data)

@ecole_controllers.get(**response_data.get('ecole'))
async def get_ecole(
        nom: str,
        presenter: EcolePresenter = Depends(get_presenter),
):
    return await presenter.get_ecole(ecole_slug=nom)