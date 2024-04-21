from transformers import pipeline

from app.config import settings


class TranslationModel(object):

    model_checkpoint = settings.translation_model_checkpoint
    model = pipeline("translation", model=model_checkpoint)
    model_path: str = model_checkpoint

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TranslationModel, cls).__new__(cls)
        return cls.instance

    def __call__(self, x):
        response = self.model([x])[0]
        return response

    def reload_model(self, model_checkpoint):
        self.model = pipeline("translation", model=model_checkpoint)
        self.model_path = model_checkpoint


class SentimentModel(object):

    model_checkpoint = settings.sentiment_model_checkpoint
    model = pipeline("sentiment-analysis", model=model_checkpoint)
    model_path: str = model_checkpoint

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SentimentModel, cls).__new__(cls)
        return cls.instance

    def __call__(self, x):
        response = self.model([x])
        return response

    def reload_model(self, model_checkpoint):

        self.model = pipeline("sentiment-analysis", model=model_checkpoint)
        self.model_path = model_checkpoint
