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