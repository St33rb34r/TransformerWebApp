from fastapi import APIRouter

from pydantic import BaseModel


class Message(BaseModel):
    message: str


router = APIRouter()


@router.post("/translate")
def translate(message: Message):
    if message:
        pass
    response = 'ты что!'
    return {'response': response}
