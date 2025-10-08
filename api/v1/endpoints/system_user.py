from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from core.auth import authenticate_system_user, create_access_token
from models.system_user import SystemUser
from schemas.system_user_schema import BaseSystemUser, CreateSystemUser
from core.security import generate_password_hash
from core.deps import get_session
from zoneinfo import ZoneInfo
from core.settings import settings as stt
from schemas.token_schema import Token

router = APIRouter()


@router.post(
    '/signup',
    status_code=status.HTTP_201_CREATED,
    response_model=BaseSystemUser,
    summary='Cadastra um novo usuário do sistema.',
    description='Cadastra um novo usuário para o sistema através do fornecimento de informações básicas,'
    'como um nome de usuário, nome completo, e-mail e senha.'
)
async def signup(system_user: CreateSystemUser, db: AsyncSession = Depends(get_session)) -> BaseSystemUser:

    hashed_password: str = generate_password_hash(system_user.password)

    try:
        new_system_user: SystemUser = SystemUser(
            username=system_user.username,
            full_name=system_user.full_name,
            email=system_user.email,
            hashed_password=hashed_password
        )

        db.add(new_system_user)
        await db.commit()
    except IntegrityError as err:
        await db.rollback()

        if hasattr(err.orig, 'sqlstate') and err.orig.sqlstate == '23505':
            error_message = str(err.orig)
            print(type(err.orig))

            if 'system_users_email_key' in error_message:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail={
                        'field': 'email',
                        'message': 'Este e-mail já está cadastrado.'
                    }
                )
            elif 'system_users_username_key' in error_message:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail={
                        'field': 'username',
                        'message': 'Este username já está cadastrado.'
                    }
                )

    return new_system_user


@router.post(
    '/login',
    status_code=status.HTTP_200_OK,
    response_model=Token,
    summary='Realiza o login do usuário.',
    description='O usuário fornece seu e-mail e senha, recebendo o token JWT e assim estar autorizado a utilizar o sistema.'
)
async def signin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: AsyncSession = Depends(get_session)) -> Token:
    system_user: BaseSystemUser = await authenticate_system_user(
        form_data.username, form_data.password, db)

    access_token_expires = timedelta(
        minutes=float(stt.ACCESS_TOKEN_EXPIRE_MINUTES))

    payload: dict[str, any] = {
        'sub': str(system_user.id),
        'username': system_user.username,
        'email': system_user.email,
        'iat': datetime.now(tz=ZoneInfo('America/Sao_Paulo')).timestamp()
    }

    access_token: str = create_access_token(
        data=payload, expires_delta=access_token_expires)

    return Token(access_token=access_token, token_type='bearer')
