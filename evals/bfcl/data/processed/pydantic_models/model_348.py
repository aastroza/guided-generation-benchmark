# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:43:40+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CreatePlayerProfile(BaseModel):
    player_name: str = Field(..., description='The desired name of the player.')
    field_class: str = Field(
        ..., alias='_class', description='The character class for the player'
    )
    starting_level: Optional[int] = Field(
        1, description='The starting level for the player'
    )
