from fastapi import FastAPI
from api.v1.api import api_router
from core.settings import settings

app = FastAPI(title='Desafio DM Card')

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)
