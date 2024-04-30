# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:32+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CalculateTriangleArea(BaseModel):
    base: int = Field(..., description='The base of the triangle.')
    height: int = Field(..., description='The height of the triangle.')
    unit: Optional[str] = Field(
        'units', description="The unit of measure (defaults to 'units' if not specified)"
    )