from models.feedback import *
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

# async session is important to manage the database
class Serializers:
    async def get_all_data(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(Feedback).order_by(Feedback.date_created) # make a statement to select all the feedbacks from the database and order them by data_created column

            result = await session.execute(statement) # execute the statement

            return result.scalars().all() # return the data as list of items
        
    async def add_data(self, async_session: async_sessionmaker[AsyncSession], feedback: Feedback):
        async with async_session() as session:
            session.add(feedback) # make a session to add the feedback from the parameter to the database
            await session.commit() # send the session
        