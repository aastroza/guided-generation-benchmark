# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:59+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class MusicGeneratorGenerateScaleProgression(BaseModel):
    key: str = Field(
        ..., description='The key in which to generate the scale progression.'
    )
    tempo: int = Field(..., description='The tempo of the scale progression in BPM.')
    duration: int = Field(..., description='The duration of each note in beats.')
    scale_type: Optional[str] = Field(
        'major', description="The type of scale to generate. Defaults to 'major'."
    )