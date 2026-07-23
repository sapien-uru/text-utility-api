from openai import(
    OpenAI,
    APITimeoutError,
    APIConnectionError,
    AuthenticationError,
    RateLimitError,
    APIStatusError,
)

from app.core.config import OPENROUTER_API_KEY, OPENROUTER_MODEL

client=OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    timeout=10.0,
)


def summarise_text(text:str) -> str:
    """Generate a concise summary using OpenRouter."""

    try:
        response=client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes text in a clear and concise way.",
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
            temperature=0.3,
            max_tokens=100,
        )

        summary=response.choices[0].message.content

        if not summary:
            raise ValueError("LLM returned an empty response.")

        return summary.strip()

    except APITimeoutError:
        raise TimeoutError("The LLM request timed out.")

    except APIConnectionError:
        raise ConnectionError("Unable to connect to OpenRouter.")

    except AuthenticationError:
        raise PermissionError("Invalid OpenRouter API key.")

    except RateLimitError:
        raise RuntimeError("Rate limit exceeded.")

    except APIStatusError as e:
        raise RuntimeError(f"OpenRouter API error: {e.status_code}")

    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")