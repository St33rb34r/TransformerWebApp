from fastapi import FastAPI

from routers import model


app = FastAPI()

app.include_router(model.router)


@app.get("/")
def root():
    return {"message": "Hello world"}