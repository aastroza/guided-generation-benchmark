# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:51+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ProbabilityDiceRoll(BaseModel):
    desired_number: int = Field(..., description='The number you want to roll.')
    number_of_rolls: int = Field(
        ..., description='How many times you want to roll that number in a row.'
    )
    die_sides: Optional[int] = Field(
        6, description='The number of sides on the die (optional; default is 6).'
    )