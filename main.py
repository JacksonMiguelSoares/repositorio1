from fastapi import FastAPI
import random

app = FastAPI()

#uvicorn main:app --reload --port 8080
@app.get("/")
async def root():
    return {"message": "Te amo"}
@app.get("/nat")
async def testenati():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}
