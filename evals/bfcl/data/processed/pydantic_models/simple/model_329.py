# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class MonopolyOddsCalculator(BaseModel):
    number: int = Field(
        ..., description='The number for which the odds are calculated.'
    )
    dice_number: int = Field(
        ..., description='The number of dice involved in the roll.'
    )
    dice_faces: Optional[int] = Field(
        6,
        description='The number of faces on a single die. Default is 6 for standard six-faced die.',
    )
