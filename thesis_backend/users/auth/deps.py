from fastapi import Depends, status
from .schemas import TokenSchema
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db_session
from .repositories import UserRepositories
from .password_service import PasswordService
from .token_service import TokenService
from .email_service import EmailService
from settings import get_settings
password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


async def get_option_presenter(session: AsyncSession = Depends(get_db_session)
        ):
    settings = get_settings()
    yield {
        'repository': UserRepositories(session=session),
        'password_service': PasswordService(context=password_context),
        'token_service': TokenService(),
        'email_service': EmailService(
            smtp_server=settings.smtp_server,
            smtp_port=settings.smtp_port,
            smtp_username=settings.smtp_username,
            smtp_password=settings.smtp_password,
            from_email=settings.from_email
        )
    }


async def get_token_service_data():
    yield {
        'token_service': TokenService()
    }



response_data = {
    'login': {
        'path': '/login',
        'status_code': status.HTTP_200_OK,
        'response_model': TokenSchema
    },
    'signup': {
        'path': '/signup',
        'status_code': status.HTTP_201_CREATED
    },
    'create_token': {
        'path': '/receive_token',
        'status_code': status.HTTP_201_CREATED,
        'response_model': TokenSchema
    },
    'request_password_reset': {
        'path': '/request-password-reset',
        'response_model': dict,
        'summary': 'Request password reset',
        'description': 'Endpoint to request a password reset',
    },
    'reset_password': {
        'path': '/reset-password',
        'response_model': dict,
        'summary': 'Reset password',
        'description': 'Endpoint to reset password with a token',
    }


}
