# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:20+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class EcologyGetTurtlePopulation(BaseModel):
    location: str = Field(..., description='The name of the location.')
    year: Optional[int] = Field(
        2001, description='The year of the data requested. Default is 2001.'
    )
    species: Optional[bool] = Field(
        False, description='Whether to include species information. Default is false.'
    )
