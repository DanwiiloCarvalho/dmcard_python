from datetime import datetime
from core.settings import settings as stt
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, DateTime, String
from sqlalchemy.sql import func

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User


class Address(stt.DBBaseModel):
    __tablename__ = 'addresses'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    street: Mapped[str] = mapped_column(String(100), nullable=False)

    number: Mapped[str] = mapped_column(String(100), nullable=False)

    area: Mapped[str] = mapped_column(String(100), nullable=False)

    city: Mapped[str] = mapped_column(String(100), nullable=False)

    state: Mapped[str] = mapped_column(String(2), nullable=False)

    cep: Mapped[str] = mapped_column(String(10), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now())

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now())

    users: Mapped[list['User']] = relationship(
        back_populates='address', lazy='joined')

    def __repr__(self):
        return f'Nome usuário: {self.name}\nRenda: {self.income}'
