from core.database import async_engine, settings
from core.deps import get_session
import asyncio

from models.status import Status


async def create_tables() -> None:
    import models._all_models

    async with async_engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)

    async for session in get_session():
        status = [
            Status(value="Reprovado"),
            Status(value="Aprovado com limite fixo"),
            Status(value="Aprovado com limite proporcional"),
            Status(value="Aprovado com limite elevado"),
            Status(value="Aprovado sem limite real")
        ]

        session.add_all(status)
        await session.commit()

if __name__ == '__main__':
    asyncio.run(create_tables())
