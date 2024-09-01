from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"Welcome":
            f"Welcome to my Docker Image  \nWe shall soon be carrying out a bunch of preflight checks so strap right in :)"}


