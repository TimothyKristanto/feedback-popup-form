from fastapi import FastAPI
from seralizers import *
from sqlalchemy.ext.asyncio import async_sessionmaker
from db import engine
from schemas import *
from typing import List
from models.feedback import *
from http import HTTPStatus

# give an API documentation design
app = FastAPI(
    title="Feedback Form API",
    description="API for the feedback form popup MultitudeX technical test",
    docs_url="/"
)

# declare async session
session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

db = Serializers()

# get all the feedbacks
@app.get("/feedbacks", response_model=List[FeedbackModel])
async def get_feedbacks():
    feedbacks = await db.get_all_data(session)
    return feedbacks

# add new feedback
@app.post("/feedbacks", status_code=HTTPStatus.CREATED)
async def add_feedback(feedback_data: CreateFeedbackModel):
    new_feedback = Feedback(
        rating = feedback_data.rating
    )

    feedbacks = await db.add_data(session, new_feedback)

    return feedbacks