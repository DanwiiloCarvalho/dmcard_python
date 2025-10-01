from time import time
from fastapi import FastAPI, Request, status, __version__
from fastapi.responses import HTMLResponse, JSONResponse
from api.v1.api import api_router
from core.settings import settings
from sqlalchemy.exc import InterfaceError, DBAPIError

app = FastAPI(
    title='Desafio DM Card',
    description='Aplicação que permitirá a solicitação de um cartão de crédito, '
    'onde o usuário irá inserir suas informações básicas e o sistema irá fazer uma '
    'análise da liberação do cartão.',
    version='1.0.0'
)

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>Desafio DMCard no Render</title>
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Desafio DM Card</h1>
            <h2>Versão do FastAPI: {__version__}</h2>
            <p>Documentação:</p>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
        </div>
    </body>
</html>
"""


@app.get(
    '/',
    tags=['Homepage'],
    summary='Rota raíz',
    description='Rota raíz para a página de apresentação da API, fornecendo os links para as documentações.'
)
async def root():
    return HTMLResponse(html)

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

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)
