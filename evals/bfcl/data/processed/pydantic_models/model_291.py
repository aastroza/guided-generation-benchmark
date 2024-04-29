# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:42:59+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class MusicGeneratorGenerateMelody(BaseModel):
    key: str = Field(..., description="The key of the melody. E.g., 'C' for C major.")
    start_note: str = Field(
        ...,
        description="The first note of the melody, specified in scientific pitch notation. E.g., 'C4'.",
    )
    length: int = Field(..., description='The number of measures in the melody.')
    tempo: Optional[int] = Field(
        None,
        description='The tempo of the melody, in beats per minute. Optional parameter. If not specified, defaults to 120.',
    )
