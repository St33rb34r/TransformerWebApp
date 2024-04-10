from fastapi import FastAPI

from transformers import pipeline

from router import transformers


app = FastAPI()
app.include_router(transformers.router)

#classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"status": "healthy"}


#@app.get("/generate")
#def generate(message: str):
    #response = classifier(message)
    #return response
