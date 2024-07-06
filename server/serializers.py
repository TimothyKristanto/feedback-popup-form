from models.feedback import *
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

# async session is important to manage the database
class Serializers:
    async def get_all_data(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(Feedback).order_by(Feedback.date_created)

            result = await session.execute(statement)

            return result.scalars().all() # return the data as list of items
        
    async def add_data(self, async_session: async_sessionmaker[AsyncSession], feedback: Feedback):
        async with async_session() as session:
            session.add(feedback)
            await session.commit()