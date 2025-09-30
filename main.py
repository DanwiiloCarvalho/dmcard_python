from time import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.v1.api import api_router
from core.settings import settings
from sqlalchemy.exc import InterfaceError, DBAPIError
from fastapi import status

app = FastAPI(
    title='Desafio DM Card',
    description='Aplicação que permitirá a solicitação de um cartão de crédito, '
    'onde o usuário irá inserir suas informações básicas e o sistema irá fazer uma '
    'análise da liberação do cartão.',
    version='1.0.0'
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)
