from fastapi import FastAPI

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Te amo"}

@app.get("/funcaoteste")
async def testenati():
    return {"message": "funciona graças a Deus"}
