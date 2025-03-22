from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Te amo"}

@app.get("/funcaoteste")
async def teste():
    return {"teste": True, "num_aleatorio": random.randint(0, 20000)}
