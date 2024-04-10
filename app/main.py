from fastapi import FastAPI
from .router import transformers


app = FastAPI()
app.include_router(transformers.router)


@app.get("/")
def root():
    return {"status": "healthy"}
