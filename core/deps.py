from typing import AsyncGenerator
from core.database import Session


async def get_session() -> AsyncGenerator:
    async with Session() as session:
        yield session
