from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sentiment_model_checkpoint: str = ""
    translation_model_checkpoint: str = ""


settings = Settings()
