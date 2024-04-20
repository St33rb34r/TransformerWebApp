from fastapi import APIRouter

from pydantic import BaseModel
from transformers import pipeline

from app.config import settings


class Message(BaseModel):
    message: str


model_checkpoint = settings.translation_model_checkpoint
translator = pipeline("translation", model=model_checkpoint)

router = APIRouter()
route = "/transformers"


@router.get(route + "/info")
def get_info():
    return {'info': 'Endpoint serves a seq2seq model, fine-tuned for translating',
            'model': settings.translation_model_checkpoint,
            'version': '-'}


@router.post(route + "/translate")
def translate(message: Message):
    if message:
        response = translator([message.message])[0]
    else:
        response = {'response': "You need to input a text to be translated. "}
    return response


