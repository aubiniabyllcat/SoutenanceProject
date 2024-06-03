from fastapi import APIRouter, Depends
from .presenter import EnseignantPresenter
from .schemas import CreateEnseignantSchema, UpdateEnseignantSchema
from .deps import response_data, get_user, get_presenter, \
   get_slug_user, get_updated_data_slug_user, get_limit_offset_user,  \
    get_create_data_user

enseignant_controllers = APIRouter(prefix='/enseignants', tags=['enseignants'])


@enseignant_controllers.get(**response_data.get('enseignants'))
async def get_enseignants(
        user=Depends(get_user),
        presenter: EnseignantPresenter = Depends(get_presenter),
        limit: int | None = 20, offset: int | None = 0
):
    data: dict = await get_limit_offset_user(user.id, limit, offset)
    return await presenter.get_enseignants(**data)

@enseignant_controllers.post(**response_data.get('create_enseignants'))
async def create_enseignant(
        enseignant_data: CreateEnseignantSchema,
        presenter: EnseignantPresenter = Depends(get_presenter),
):
    data: dict = await get_create_data_user( enseignant_data)
    return await presenter.create_enseignant(**data)

@enseignant_controllers.delete(**response_data.get('delete_enseignants'))
async def delete_enseignant(
        matricule: str, user=Depends(get_user),
        presenter: EnseignantPresenter = Depends(get_presenter),
):
    data: dict = await get_slug_user(matricule, user.id)
    return await presenter.delete_enseignant(**data)

@enseignant_controllers.patch(**response_data.get('update_enseignant'))
async def update_enseignant(
        updated_data: UpdateEnseignantSchema,
        matricule: str, user=Depends(get_user),
        presenter: EnseignantPresenter = Depends(get_presenter),
):
    data: dict = await get_updated_data_slug_user(
        updated_data, matricule, user.id)
    return await presenter.update_enseignant(**data)

@enseignant_controllers.get(**response_data.get('enseignant'))
async def get_enseignant(
        matricule: str,
        presenter: EnseignantPresenter = Depends(get_presenter),
):
    return await presenter.get_enseignant(enseignant_slug=matricule)