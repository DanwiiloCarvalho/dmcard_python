from datetime import date, datetime
from decimal import Decimal
from core.settings import settings as stt
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, Integer, Numeric, DateTime, String
from sqlalchemy.sql import func
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.address import Address
    from models.card_request import CardRequest


class User(stt.DBBaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    birth_date: Mapped[date] = mapped_column(Date, nullable=False)

    cpf: Mapped[str] = mapped_column(String(11), nullable=False)

    occupation: Mapped[str] = mapped_column(String(45), nullable=False)

    income: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    address_id: Mapped[int] = mapped_column(
        ForeignKey('addresses.id'), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now())

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now())

    card_requests: Mapped[list['CardRequest']] = relationship(
        back_populates='user', lazy='joined')

    address: Mapped['Address'] = relationship(
        back_populates='users', lazy='joined')

    def __repr__(self):
        return f'Nome usuário: {self.name}\nRenda: {self.income}'
