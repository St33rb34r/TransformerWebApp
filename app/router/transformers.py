from fastapi import APIRouter

from transformers import pipeline
from pydantic import BaseModel


class Message(BaseModel):
    message: str


model_checkpoint = "Helsinki-NLP/opus-mt-en-fr"
translator = pipeline("translation", model=model_checkpoint)

#translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")

router = APIRouter()


@router.post("/translate")
def translate(message: Message()):
    response = translator(message)
    return response[0]
