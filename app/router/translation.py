from fastapi import APIRouter

from pydantic import BaseModel

from app.ml_model import TranslationModel


class Message(BaseModel):
    message: str


router = APIRouter()
route = "/translation"


@router.get(route + "/info")
def get_info():
    return {'info': 'Endpoint serves a seq2seq model, fine-tuned for translating',
            'model': TranslationModel().model_path,
            'version': '-'}


@router.post(route + "/translate")
def translate(message: Message):
    translator = TranslationModel()
    if message:
        response = translator([message.message])[0]
    else:
        response = {'response': "You need to input a text to be translated. "}
    return response


@router.put(route + "/load_model")
def load_translation_model(model_checkpoint: str):
    model = TranslationModel()
    model.reload_model(model_checkpoint)
    return {"response": "success"}, 200


