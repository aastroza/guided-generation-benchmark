# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:43:06+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class MusicCalculateNoteDuration(BaseModel):
    first_note_frequency: int = Field(
        ..., description='The frequency of the first note in Hz.'
    )
    second_note_frequency: int = Field(
        ..., description='The frequency of the second note in Hz.'
    )
    tempo: Optional[int] = Field(
        None,
        description='The tempo of the music in beats per minute. Defaults to 120 beats per minute.',
    )
