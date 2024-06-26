# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:02+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CalculateElectricFieldStrength(BaseModel):
    charge: float = Field(
        ..., description='The charge in Coulombs. This is a float type value.'
    )
    distance: int = Field(..., description='The distance from the charge in meters.')
    medium: Optional[str] = Field(
        'vacuum',
        description="The medium in which the charge and the point of calculation is located. Default is 'vacuum'.",
    )
