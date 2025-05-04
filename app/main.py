from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.rag import get_answer

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    answer = get_answer(query.question)
    return {"answer": answer}
