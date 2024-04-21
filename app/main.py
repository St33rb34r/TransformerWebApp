from fastapi import FastAPI
from app.router import translation, sentiment


app = FastAPI(root_path='/prod')    # To make /docs accessible from AWS

app.include_router(translation.router)
app.include_router(sentiment.router)


@app.get("/")
def root():
    return {"status": "healthy"}