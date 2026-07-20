import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app= FastAPI()

class TextRequest(BaseModel):
    text:str
    
@app.post("/analyse/basic")
def analyse_basic(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text Cannot be Empty."
        )
    text=request.text
    words=text.split()
    word_count=len(words)
    character_count=len(text)
    reading_time=round(word_count/200,2)

    return{
        "word_count":word_count,
        "chareacter_count":character_count,
        "reading_time_minutes":reading_time
    }
@app.post("/analyse/sentences")
def analyse_sentences(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty."
        )
    text=request.text.strip()

    sentences=[s.strip() for s in re.split(r"[.!?]+",text) if s.strip()]

    sentence_count=len(sentences)
    word=text.split()
    word_count=len(word)
    average_sentence_length=round(word_count/sentence_count,2)

    return{
        "sentence_count":sentence_count,
        "average_sentence_length":average_sentence_length
    }
