from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from database import get_db_session
from users.auth.email_service import EmailService
from users.auth.password_service import PasswordService
from users.auth.repositories import UserRepositories
from users.auth.token_service import TokenService
from .schemas import CreateUserSchema, BaseUserAccountSchema, ResetPasswordConfirmSchema, ResetPasswordRequestSchema
from .presenter import UserPresenter, TokenPresenter
from .deps import get_option_presenter, response_data, get_token_service_data
from sqlalchemy.ext.asyncio import  AsyncSession

auth_controllers = APIRouter(prefix='/auth', tags=['users'])


@auth_controllers.post(**response_data.get('signup'))
async def sign_up(
        users_data: CreateUserSchema,
        option_presenter=Depends(get_option_presenter),
        session: AsyncSession = Depends(get_db_session)
):
    return await UserPresenter(session=session,**option_presenter) \
        .sign_up(**users_data.dict())




@auth_controllers.post(**response_data.get('login'))
async def login(
        #form_data: CreateUserSchema,
        form_data: OAuth2PasswordRequestForm = Depends(),
        option_presenter=Depends(get_option_presenter),
):
    #breakpoint()
    return await UserPresenter(**option_presenter) \
        .login(username=form_data.username, password=form_data.password)


@auth_controllers.post(**response_data.get('create_token'))
async def get_token(
    
        username: BaseUserAccountSchema,
        token_data=Depends(get_token_service_data)
):
    return await TokenPresenter(**token_data) \
        .get_token(username=username.username)

@auth_controllers.post("/request-password-reset", response_model=dict)
async def request_password_reset(
        request: ResetPasswordRequestSchema,
        option_presenter=Depends(get_option_presenter)
):
    user_presenter = UserPresenter(**option_presenter)
    return await user_presenter.request_password_reset(username=request.username)


@auth_controllers.post("/reset-password", response_model=dict)
async def reset_password(
        request: ResetPasswordConfirmSchema,
        option_presenter=Depends(get_option_presenter)
):
    user_presenter = UserPresenter(**option_presenter)
    return await user_presenter.reset_password(token=request.token, new_password=request.new_password)