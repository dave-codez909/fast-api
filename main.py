from fastapi import FastAPI
from pydantic import BaseModel

class response(BaseModel):
    message: str

app = FastAPI()

@app.get("/")
def home():
    data ={"message": "Welcome to the FastAPI ",
        
    }
    return data

@app.post("/message")
def text(user_text :response):
    data ={
        "response": user_text
    }
    return data