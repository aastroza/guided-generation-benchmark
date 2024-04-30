# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:31+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GenerateCircleImage(BaseModel):
    radius: int = Field(..., description='The radius of the circle in pixels.')
    color: str = Field(..., description='The color of the circle.')
    background: Optional[str] = Field(
        'white', description='Optional: The color of the background, default is white.'
    )