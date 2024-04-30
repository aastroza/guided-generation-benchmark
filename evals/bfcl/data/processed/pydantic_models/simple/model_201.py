# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:53+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class EstimatePopulation(BaseModel):
    species: str = Field(
        ..., description='The species for which population needs to be estimated.'
    )
    country: str = Field(..., description='The country where the species lives.')
    year: Optional[int] = Field(
        2024,
        description='The year for which population estimate is sought. Default is the current year.',
    )