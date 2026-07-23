# Text Utility API

A FastAPI-based REST API for text analysis and AI-powered summarization.

## Features

- Word Count
- Character Count
- Sentence Analysis
- Keyword Extraction
- AI Text Summarization (OpenRouter)

---

## Installation

```bash
git clone <repo-url>
cd text-utility-api

python -m venv .venv
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
OPENROUTER_API_KEY=*****
OPENROUTER_MODEL=deepseek/deepseek-chat-v3-0324:free
```

---

## Run

```bash
uvicorn app.main:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## Endpoints

### POST `/analyse/basic`

Returns:

- Word count
- Character count
- Reading time

---

### POST `/analyse/sentences`

Returns:

- Sentence count
- Average sentence length

---

### POST `/analyse/keywords`

Returns the top keywords.

---

### POST `/analyse/summarise`

Request

```json
{
  "text": "Artificial Intelligence is changing software development..."
}
```

Response

```json
{
  "summary": "Artificial intelligence is improving software development by helping developers write code and automate tasks."
}
```

---

## Tech Stack

- FastAPI
- Pydantic
- OpenRouter
- OpenAI Python SDK
- Python