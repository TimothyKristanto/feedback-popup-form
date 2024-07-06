from pydantic import BaseModel
from datetime import datetime

# pydantic model for create new feedback
class CreateFeedbackModel(BaseModel):
    rating: int