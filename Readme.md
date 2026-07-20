# 📝 Text Utility API

A REST API built with FastAPI that performs basic text analysis.

## Features

- Word count
- Character count
- Estimated reading time
- Sentence count
- Average sentence length
- Top 5 keyword extraction

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Installation

```bash
git clone https://github.com/<your-username>/text-utility-api.git
cd text-utility-api

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

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

### POST /analyse/sentences

Response

```json
{
  "sentence_count": 1,
  "average_sentence_length": 2.0
}
```

---

### POST /analyse/keywords

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