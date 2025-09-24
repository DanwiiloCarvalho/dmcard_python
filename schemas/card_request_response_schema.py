from decimal import Decimal
from pydantic import BaseModel as SCBaselModel
from pydantic import field_validator


class CardRequestResponseSchema(SCBaselModel):
    id: int
    credit_score: int
    credit_limit: Decimal | None = None
    status_id: int
    user_id: int

    @field_validator('id')
    def id_validate(cls, id: int) -> int:
        if id <= 0:
            raise ValueError('O ID deve ser positivo')
        return id

    @field_validator('credit_score')
    def credit_score_validate(cls, credit_score: int) -> int:
        if credit_score >= 1 and credit_score <= 999:
            return credit_score
        raise ValueError('A pontuação de crédito deve estar entre 1 e 999')

    @field_validator('credit_limit')
    def credit_limit_validate(cls, credit_limit: Decimal) -> Decimal:
        if credit_limit and credit_limit < 0:
            raise ValueError('O limite de crédito deve ser positivo.')
        return credit_limit

    @field_validator('status_id')
    def status_id_validate(cls, status: int) -> int:
        if status >= 1 and status <= 5:
            return status
        raise ValueError('O status deve estar entre 1 e 5.')

    @field_validator('user_id')
    def user_id_validate(cls, user_id: int) -> int:
        if user_id > 0:
            return user_id
        raise ValueError('O user_id deve ser positivo.')
