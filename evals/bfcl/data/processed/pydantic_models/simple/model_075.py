# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:24+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class ElephantPopulationEstimate(BaseModel):
    current_population: int = Field(..., description='The current number of elephants.')
    growth_rate: float = Field(
        ...,
        description='The annual population growth rate of elephants. This is a float type value.',
    )
    years: int = Field(
        ..., description='The number of years to project the population.'
    )