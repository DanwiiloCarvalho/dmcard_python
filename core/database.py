from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from core.settings import settings

async_engine: AsyncEngine = create_async_engine(url=settings.DB_URL)

Session = async_sessionmaker(
    bind=async_engine, expire_on_commit=False)
