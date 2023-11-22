from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Nuxt.js runs on port 3000 by default
    "http://yourfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Can swap with domains specified in origins array
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class SignInData(BaseModel):
    username: str
    password: str

class SignUpData(BaseModel):
    username: str
    companyName: str
    password: str
    passwordConfirm: str

@app.post("/signin")
async def sign_in(data: SignInData):
    # Handle sign-in logic here
    print("Sign In Data:", data)
    return {"message": "Sign In Successful"}

@app.post("/signup")
async def sign_up(data: SignUpData):
    # Handle sign-up logic here
    #if data.password != data.passwordConfirm:
    #    raise HTTPException(status_code=400, detail="Passwords do not match")
    
    print("Sign Up Data:", data)
    return {"message": "Sign Up Successful"}
