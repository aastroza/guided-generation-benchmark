# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:38+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GetSculptureValue(BaseModel):
    sculpture: str = Field(..., description='The name of the sculpture.')
    artist: str = Field(
        ..., description='The name of the artist who created the sculpture.'
    )
    year: Optional[int] = Field(
        2024,
        description='The year the sculpture was created. This is optional and is not required for all sculptures. Default is the most recent year.',
    )
