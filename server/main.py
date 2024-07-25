from fastapi import FastAPI
from create_read_data import *
from sqlalchemy.ext.asyncio import async_sessionmaker
from db import engine
from schemas import *
from typing import List
from models.feedback import *
from http import HTTPStatus
from starlette.middleware.cors import CORSMiddleware

# Transform the page into an API documentation
app = FastAPI(
    title="Feedback Form API",
    description="API for the feedback form popup MultitudeX technical test",
    docs_url="/"
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

db = Serializers()

# get all the feedbacks from the database
@app.get("/feedbacks/{id}")
async def get_feedback_by_id(id: int):
    feedback = await db.get_data_by_id(session, id) # get all the feedbacks data from the database
    return feedback # return the feedbacks in the form of JSON

@app.get("/feedbacks")
async def get_feedbacks():
    feedbacks = await db.get_all_data(session) # get all the feedbacks data from the database
    return feedbacks # return the feedbacks in the form of JSON

# add new feedback
@app.post("/feedbacks", status_code=HTTPStatus.CREATED)
async def add_feedback(feedback_data: CreateFeedbackModel):
    # make a Feedback model to contain the feedback data
    new_feedback = Feedback(
        id = feedback_data.id,
        rating = feedback_data.rating,
    )

    # existing_feedback = await db.get_data_by_id(new_feedback.id)

    
    feedbacks = await db.add_data(session, new_feedback) # add the data to the database

    return feedbacks
    