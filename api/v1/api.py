from fastapi import APIRouter
from api.v1.endpoints import card_request, system_user

api_router = APIRouter()
api_router.include_router(
    card_request.router, prefix='/card_requests', tags=['Solicitações de cartão'])
api_router.include_router(
    system_user.router, prefix='/auth', tags=['Autenticação'])
