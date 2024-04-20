from transformers import pipeline

from fastapi import APIRouter

from pydantic import BaseModel

from app.config import settings


class Message(BaseModel):
    message: str


checkpoint = settings.sentiment_model_checkpoint
classifier = pipeline("sentiment-analysis", model=checkpoint)

router = APIRouter()
route = "/sentiment"


@router.get(route + "/info")
def get_info():
    return {'info': 'Endpoint serves a seq2seq model, fine-tuned for performing sentiment analysis',
            'model': settings.sentiment_model_checkpoint,
            'version': '-'}


@router.post(route + "/parse_sentence")
def sentiment(message: Message):
    response = classifier(message.message)[0]
    return response


