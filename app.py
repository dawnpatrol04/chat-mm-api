from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

def llm(user_message: str) -> str:
    # Placeholder for the LLM function
    return f"I hear ya. you said ... {user_message}"

@app.post("/send_message")
def send_message(msg: Message):
    response_message = llm(msg.message)
    return {"response": response_message}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chat API"}

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
