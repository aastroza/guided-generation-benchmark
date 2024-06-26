# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:27+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class CivilCasesRetrieve(BaseModel):
    year: int = Field(..., description='Year of the cases')
    crime_type: str = Field(..., description='Type of the crime.')
    location: str = Field(
        ..., description='Location of the case in the format of city name.'
    )
