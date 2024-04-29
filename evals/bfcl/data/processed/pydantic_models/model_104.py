# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:40:43+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GeometryAreaTriangle(BaseModel):
    base: int = Field(..., description='The length of the base of the triangle.')
    height: int = Field(..., description='The height of the triangle from the base.')
    unit: Optional[str] = Field(
        None,
        description='The measurement unit for the area. Defaults to square meters.',
    )
