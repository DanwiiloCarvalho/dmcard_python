from typing import Annotated, AsyncGenerator
from sqlalchemy import select
from core.settings import settings as stt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from core.database import Session
from core.auth import get_user
from sqlalchemy.ext.asyncio import AsyncSession
from models.system_user import SystemUser
from schemas.system_user_schema import BaseSystemUser
import jwt


async def get_session() -> AsyncGenerator:
    async with Session() as session:
        yield session

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f'{stt.API_V1_PREFIX}/auth/login')


async def get_logged_user(token: Annotated[str, Depends(oauth2_scheme)], db: AsyncSession = Depends(get_session)) -> BaseSystemUser:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possível validar as credenciais.',
        headers={'WWW-Authenticate': 'Bearer'}
    )

    try:
        payload = jwt.decode(
            jwt=token, algorithms=stt.ALGORITHM, key=stt.SECRET_KEY)
        if payload['sub'] is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception

    user: SystemUser = await get_user(email=payload['email'], db=db)

    if not user:
        raise credentials_exception
    return user
