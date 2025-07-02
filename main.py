from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
from db import add_flashcard, get_mixed_flashcards
from subject_model import detect_subject

app = FastAPI()


class FlashcardRequest(BaseModel):
    student_id: str
    question: str
    answer: str

# POST 
@app.post("/flashcard")
def create_flashcard(data: FlashcardRequest):
    subject = detect_subject(data.question)
    add_flashcard(data.student_id, data.question, data.answer, subject)
    return {
        "message": "Flashcard added successfully",
        "subject": subject
    }

# GET 
@app.get("/get-subject")
def get_flashcards(student_id: str = Query(...), limit: int = Query(5)) -> List[dict]:
    cards = get_mixed_flashcards(student_id, limit)
    if not cards:
        raise HTTPException(status_code=404, detail="No flashcards found for this student.")
    return cards

