from decimal import Decimal
from pydantic import BaseModel as SCBaseModel


class CardRequestGetSchema(SCBaseModel):
    id: int
    credit_score: int
    credit_limit: Decimal | None = None
    status: str
    username: str
