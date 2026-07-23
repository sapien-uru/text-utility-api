from pydantic import BaseModel, Field


class SummariseRequest(BaseModel):
    text: str=Field(
        ...,
        min_length=1,
        description="Text to be summarized",
        examples=["FastAPI is a modern Python web framework..."],
    )


class SummariseResponse(BaseModel):
    summary: str