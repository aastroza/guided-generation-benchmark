# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:23+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CalculateBacteriaEvolutionRate(BaseModel):
    start_population: int = Field(
        ..., description='The starting population of bacteria.'
    )
    duplication_frequency: int = Field(
        ..., description='The frequency of bacteria duplication per hour.'
    )
    duration: int = Field(..., description='Total duration in hours.')
    generation_time: Optional[int] = Field(
        20,
        description='The average generation time of the bacteria in minutes. Default is 20 minutes',
    )