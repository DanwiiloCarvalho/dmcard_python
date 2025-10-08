from datetime import datetime, timedelta
from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.security import verify_password
from core.settings import settings as stt
from models.system_user import SystemUser
from schemas.system_user_schema import BaseSystemUser
from zoneinfo import ZoneInfo
import jwt


async def authenticate_system_user(email: EmailStr, password: str, db: AsyncSession) -> BaseSystemUser:
    query = select(SystemUser).filter(SystemUser.email == email)

    result = await db.execute(query)
    system_user: SystemUser = result.scalar_one_or_none()

    if not system_user or not verify_password(password, system_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Credenciais inválidas.', headers={'WWW-Authenticate': 'Bearer'})

    return system_user


def create_access_token(data: dict[str, any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(ZoneInfo('America/Sao_Paulo')) + expires_delta
    else:
        expire = datetime.now(ZoneInfo('America/Sao_Paulo')
                              ) + timedelta(minutes=15)

    to_encode['exp'] = expire

    enconded_jwt = jwt.encode(
        payload=to_encode, algorithm=stt.ALGORITHM, key=stt.SECRET_KEY)

    return enconded_jwt


async def get_user(email: str, db: AsyncSession) -> SystemUser:
    query = select(SystemUser).filter(
        SystemUser.email == email)
    result = await db.execute(query)
    return result.scalar_one_or_none()
