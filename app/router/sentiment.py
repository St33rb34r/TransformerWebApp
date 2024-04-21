from transformers import pipeline

from fastapi import APIRouter

from pydantic import BaseModel

from app.config import settings
from app.ml_model import SentimentModel


class Message(BaseModel):
    message: str


router = APIRouter()
route = "/sentiment"


@router.get(route + "/info")
def get_info():

    return {'info': 'Endpoint serves a seq2seq model, fine-tuned for performing sentiment analysis',
            'model': SentimentModel().model_path,
            'version': '-'}


@router.post(route + "/get_sentiment")
def sentiment(message: Message):
    classifier = SentimentModel()
    response = classifier(message.message)[0]
    return response


@router.put(route + "/load_model")
def load_sentiment_model(model_checkpoint: str):
    model = SentimentModel()
    model.reload_model(model_checkpoint)
    return {"response": "success"}, 200
