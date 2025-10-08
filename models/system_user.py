from datetime import datetime
from sqlalchemy import DateTime, Integer, String, func
from core.settings import settings as stt
from sqlalchemy.orm import Mapped, mapped_column


class SystemUser(stt.DBBaseModel):
    __tablename__ = 'system_users'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    username: Mapped[str] = mapped_column(
        String(), nullable=False, unique=True)

    full_name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True)

    hashed_password: Mapped[str] = mapped_column(String(256), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now())

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now())
