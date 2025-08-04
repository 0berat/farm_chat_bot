from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ask_to_gemini import ask_gemini

app = FastAPI()

# CORS ayarları
origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],    
)

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(data: Question):
    answer = ask_gemini(data.question)
    return {"answer": answer}
