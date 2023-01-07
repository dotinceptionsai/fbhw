#!/usr/bin/env python
import transformers
import torch
from transformers import pipeline

from pydantic import BaseModel

from fastapi import FastAPI, Request

model="t5-base"
pipeline = pipeline("translation_en_to_de", model=model)
pipeline.save_pretrained('/data/models/' + model)

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class TextToTranslate(BaseModel):
    input_text: str

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/test")
def test():
    test = pipeline(["Hello","Goodbye"])
    return {"message": test}

@app.post("/")
async def get_body(request: Request):
    body    = await request.json()
    message = body['message']
    result  = pipeline(message)
    return {
     "result" : result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=80, reload=True)
