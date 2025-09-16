from core.database import async_engine, settings
import asyncio


async def create_tables() -> None:
    import models._all_models

    async with async_engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)

if __name__ == '__main__':
    asyncio.run(create_tables())
