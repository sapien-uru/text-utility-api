from collections import Counter
import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app= FastAPI()

STOPWORDS={
    "the","is","am","are","was","were",
    "a","an","and","or","of","to",
    "in","on","at","for","with","at",
    "this","it","as","be"
}

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

@app.post("/analyse/keywords")
def analyse_keywords(request:TextRequest):
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty."
        )
    text=request.text.lower()
    text=re.sub(r"[^a-zA-Z0-9\s]","",text)
    words=text.split()
    meaningful_words=[
        word for word in words
        if word not in STOPWORDS       
    ]
    counts=Counter(meaningful_words)
    top_keywords=[
        {"word":word,"count":count}
        for word ,count in counts.most_common(5) 
    ]

    return {
        "keywords":top_keywords
    }

