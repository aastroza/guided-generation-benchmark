# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:42+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class CalculateCircleDimensions(BaseModel):
    radius: int = Field(..., description='The radius of the circle.')
