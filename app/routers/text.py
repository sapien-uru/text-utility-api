from fastapi import APIRouter, HTTPException

from app.models import SummariseRequest, SummariseResponse
from app.services.llm import summarise_text

router = APIRouter(prefix="/analyse", tags=["Text Analysis"])


@router.post("/summarise", response_model=SummariseResponse)
def summarise(request: SummariseRequest):
    try:
        summary = summarise_text(request.text)
        return SummariseResponse(summary=summary)

    except TimeoutError as e:
        raise HTTPException(status_code=504, detail=str(e))

    except PermissionError as e:
        raise HTTPException(status_code=401, detail=str(e))

    except ConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))

    except RuntimeError as e:
        if "Rate limit" in str(e):
            raise HTTPException(status_code=429, detail=str(e))
        raise HTTPException(status_code=503, detail=str(e))

    except ValueError as e:
        raise HTTPException(status_code=502, detail=str(e))

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred."
        )