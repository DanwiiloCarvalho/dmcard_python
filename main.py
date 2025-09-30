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


@app.middleware('http')
async def db_unavailable_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except (OSError, InterfaceError, DBAPIError):
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "detail": "Banco de dados indisponível. Tente novamente mais tarde.",
                "timestamp": time(),
                "path": str(request.url.path)
            }
        )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)
