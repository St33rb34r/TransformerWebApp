from fastapi import APIRouter

#from transformers import pipeline
from pydantic import BaseModel


class Message(BaseModel):
    message: str


#model_checkpoint = "Helsinki-NLP/opus-mt-en-fr"
#translator = pipeline("translation_en_to_fr")#, model=model_checkpoint)

router = APIRouter()


@router.post("/translate")
def translate(message: Message()):
    response = 'ты что!'
    return {'response': response}
