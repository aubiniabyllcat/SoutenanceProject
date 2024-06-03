from fastapi import APIRouter, Depends
from .presenter import EtudiantPresenter
from .schemas import CreateEtudiantSchema, UpdateEtudiantSchema
from .deps import response_data, get_user, get_presenter, \
   get_slug_user, get_updated_data_slug_user, get_limit_offset_user,  \
    get_create_data_user

etudiant_controllers = APIRouter(prefix='/etudiants', tags=['etudiants'])


@etudiant_controllers.get(**response_data.get('etudiants'))
async def get_etudiants(
        user=Depends(get_user),
        presenter: EtudiantPresenter = Depends(get_presenter),
        limit: int | None = 20, offset: int | None = 0
):
    data: dict = await get_limit_offset_user(user.id, limit, offset)
    return await presenter.get_etudiants(**data)

@etudiant_controllers.post(**response_data.get('create_etudiants'))
async def create_etudiant(
        etudiant_data: CreateEtudiantSchema,
        presenter: EtudiantPresenter = Depends(get_presenter),
):
    data: dict = await get_create_data_user( etudiant_data)
    return await presenter.create_etudiant(**data)

@etudiant_controllers.delete(**response_data.get('delete_etudiants'))
async def delete_etudiant(
        matricule: str, user=Depends(get_user),
        presenter: EtudiantPresenter = Depends(get_presenter),
):
    data: dict = await get_slug_user(matricule, user.id)
    return await presenter.delete_etudiant(**data)

@etudiant_controllers.patch(**response_data.get('update_etudiant'))
async def update_etudiant(
        updated_data: UpdateEtudiantSchema,
        matricule: str, user=Depends(get_user),
        presenter: EtudiantPresenter = Depends(get_presenter),
):
    data: dict = await get_updated_data_slug_user(
        updated_data, matricule, user.id)
    return await presenter.update_etudiant(**data)

@etudiant_controllers.get(**response_data.get('etudiant'))
async def get_etudiant(
        matricule: str,
        presenter: EtudiantPresenter = Depends(get_presenter),
):
    return await presenter.get_etudiant(etudiant_slug=matricule)