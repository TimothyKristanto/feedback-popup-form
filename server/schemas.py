from pydantic import BaseModel
from datetime import datetime

# pydantic model for get all feedbacks
class FeedbackModel(BaseModel):
    id: int
    rating: int
    date_created: datetime

# pydantic model for create new feedback
class CreateFeedbackModel(BaseModel):
    rating: int