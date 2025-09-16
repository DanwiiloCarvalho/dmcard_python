from sqlalchemy.sql import func
from sqlalchemy import Integer, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.settings import settings as stt
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.card_request import CardRequest


class Status(stt.DBBaseModel):
    __tablename__ = 'status'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    value: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now())

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now())

    card_requests: Mapped[list['CardRequest']
                          ] = relationship(back_populates='status', lazy='joined')

    def __repr__(self):
        return f'Valor status: {self.value}'
