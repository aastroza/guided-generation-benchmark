# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:03+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class SentimentAnalysis(BaseModel):
    text: str = Field(
        ..., description='The text on which to perform sentiment analysis.'
    )
    language: str = Field(..., description='The language in which the text is written.')