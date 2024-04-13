from transformers import pipeline

from fastapi import APIRouter

from pydantic import BaseModel


class Message(BaseModel):
    message: str


classifier = pipeline("sentiment-analysis", model="app/models/test_transformer")

router = APIRouter()


@router.post("/sentiment")
def sentiment(message: Message):
    response = classifier(message.message)[0]
    return response
