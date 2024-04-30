# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:37+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class SculptureSearch(BaseModel):
    location: str = Field(..., description='The city where the sculptures are located.')
    time_frame: str = Field(
        ..., description='The time frame during which the sculptures were made.'
    )
    material: Optional[str] = Field(
        'all', description="Optional material of the sculptures. Default is 'all'"
    )
