from pydantic import BaseModel
from typing import List

class AnswerRequest(BaseModel):
    session_id: str
    question: str
    answer: str

class InterviewResponse(BaseModel):
    next_question: str
    score: int
    feedback: str
