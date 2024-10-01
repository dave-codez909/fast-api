from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


USERS_DB = {

    "david": {
        "username": "david",
        "password": "toothbrush"
    }
}


class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(request: LoginRequest):
    username = request.username
    password = request.password
    
    
    if username not in USERS_DB:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    
    if USERS_DB[username] != password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    return {"message": "Login successful"}
