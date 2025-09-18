from datetime import datetime
from decimal import Decimal
from core.settings import settings as stt
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Numeric, DateTime
from sqlalchemy.sql import func
from typing import TYPE_CHECKING
from models.status import Status

if TYPE_CHECKING:
    from models.user import User


class CardRequest(stt.DBBaseModel):
    __tablename__ = 'card_requests'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    credit_score: Mapped[int] = mapped_column(Integer, nullable=False)

    credit_limit: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=True)

    status_id: Mapped[int] = mapped_column(
        ForeignKey('status.id'), nullable=False)

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now())

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now())

    status: Mapped['Status'] = relationship(
        back_populates='card_requests', lazy='joined')

    user: Mapped['User'] = relationship(
        back_populates='card_requests', lazy='joined')

    def __repr__(self):
        return f'ID usuário: {self.user_id}\nID Status: {self.status_id}'
