# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:42:36+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class CalculatePaintNeeded(BaseModel):
    coverage_rate: int = Field(
        ..., description='The area in square feet that one gallon of paint can cover.'
    )
    length: int = Field(..., description='Length of the wall to be painted in feet.')
    height: int = Field(..., description='Height of the wall to be painted in feet.')
