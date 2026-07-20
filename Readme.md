# Tect Utility API

A REST API built with FastAPI that performs basic text analysis.

## Features 
-Word count
-Character count
-Estimated reading time
-Sentence count
-Average Sentence Length
-Top 5 Keyword extraction

## Tech Stack
-Python
-FastAPI
-Pydantic
-Uvicorn

## Installation
git clone https://github.com/ /tex-utility-api.git
cd text-utlity-api

python -m venv .venv

# Windows
.venv/Scripts/Activate/ps1

pip install -r requiremnts.txt

## Run 
uvicorn app.main:app --reload

SERVER:
https://127.0.0.1:8000

Swagger UI:
https://127.0.0.1:8000/docs

## API Endpoints

### POST /analyse/basic


Request

```json
{
  "text": "Hello world"
}
```

Response

```json
{
  "word_count": 2,
  "character_count": 11,
  "reading_time_minutes": 0.01
}
```

---

### POST /analyze/sentences

Response

```json
{
  "sentence_count": 1,
  "average_sentence_length": 2.0
}
```

---

### POST /analyze/keywords

Response

```json
{
  "keywords": [
    {
      "word": "hello",
      "count": 1
    },
    {
      "word": "world",
      "count": 1
    }
  ]
}
```

## License

MIT