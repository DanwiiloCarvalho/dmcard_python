from decimal import Decimal
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from models.address import Address
from models.user import User
from models.card_request import CardRequest
from schemas.card_request_create_schema import CardRequestCreateSchema
from schemas.card_request_response_schema import CardRequestResponseSchema
from core.deps import get_session
import random

from schemas.card_request_get_schema import CardRequestGetSchema

router = APIRouter()


@router.post('', status_code=status.HTTP_201_CREATED, response_model=CardRequestResponseSchema)
async def add_card_request(card_request: CardRequestCreateSchema, db: AsyncSession = Depends(get_session)) -> CardRequestResponseSchema:
    new_address: Address = Address(
        street=card_request.address.street,
        number=card_request.address.number,
        area=card_request.address.area,
        city=card_request.address.city,
        state=card_request.address.state,
        cep=card_request.address.cep
    )

    new_user: User = User(
        name=card_request.name,
        birth_date=card_request.birth_date,
        cpf=card_request.cpf,
        occupation=card_request.occupation,
        income=card_request.income,
    )
    new_user.address = new_address

    credit_score: int = random.randint(1, 999)
    credit_limit: Decimal | None = None
    new_status: int = 1

    if credit_score >= 300 and credit_score <= 599:
        credit_limit = 1_000.00
        new_status = 2
    if credit_score >= 600 and credit_score <= 799:
        credit_limit = Decimal('50') / Decimal('100') * card_request.income
        if credit_limit < 1_000.00:
            credit_limit = 1_000.00
        new_status = 3
    if credit_score >= 800 and credit_score <= 950:
        credit_limit = Decimal('2') * card_request.income
        new_status = 4
    if credit_score >= 951 and credit_score <= 999:
        credit_limit = 1_000_000.00
        new_status = 5

    new_card_request: CardRequest = CardRequest(
        credit_score=credit_score,
        credit_limit=credit_limit,
        status_id=new_status
    )

    new_card_request.user = new_user
    db.add(new_card_request)
    await db.commit()
    return new_card_request


@router.get('', status_code=status.HTTP_200_OK, response_model=list[CardRequestGetSchema])
async def get_card_requests(db: AsyncSession = Depends(get_session)) -> list[CardRequestGetSchema]:
    query = select(CardRequest).order_by(desc(CardRequest.created_at))
    result = await db.execute(query)
    card_requests: list[CardRequest] = result.scalars().unique().all()

    if not card_requests:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return [
        CardRequestGetSchema(
            id=request.id,
            credit_score=request.credit_score,
            credit_limit=request.credit_limit,
            status=request.status.value,
            username=request.user.name
        )
        for request in card_requests
    ]
