from fastapi import APIRouter
from api.v1.endpoints import address
from api.v1.endpoints import card_request

api_router = APIRouter()
api_router.include_router(card_request.router, prefix='/card_requests')
