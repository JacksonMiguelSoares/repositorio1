from fastapi import FastAPI

app = FastAPI()

#uvicorn main:app --reload --port 8080
@app.get("/")
async def root():
    return {"message": "Te amo"}
@app.get("/nat")
async def testenati():
    return {"message": "funciona graças a Deus"}
