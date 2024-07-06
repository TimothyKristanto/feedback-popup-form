from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()

# create an engine to connect to the database in order to manage the database
engine = create_async_engine(
    url = os.getenv("DATABASE_URL"), # load the database
    echo = True # show sql logs
)

# Base class for models to inherit
class Base(DeclarativeBase):
    pass