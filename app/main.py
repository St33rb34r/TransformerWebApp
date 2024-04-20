from fastapi import FastAPI
from .router import transformers, sentiment


app = FastAPI(root_path='/prod')    # To make /docs accessible from AWS

app.include_router(transformers.router)
app.include_router(sentiment.router)


@app.get("/")
def root():
    return {"status": "healthy"}