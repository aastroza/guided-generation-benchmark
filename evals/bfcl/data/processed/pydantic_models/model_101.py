# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:40:41+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CalculateSpeed(BaseModel):
    distance: int = Field(
        ..., description='The distance the object travelled in meters.'
    )
    time: int = Field(
        ..., description='The time it took for the object to travel in seconds.'
    )
    to_unit: Optional[str] = Field(
        None,
        description='The unit in which the speed should be calculated, default is m/s.',
    )
