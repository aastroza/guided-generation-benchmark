# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class BoardGameChessGetTopPlayers(BaseModel):
    location: str = Field(
        ..., description='The city you want to find the players from.'
    )
    minimum_rating: int = Field(
        ..., description='Minimum rating to filter the players.'
    )
    number_of_players: Optional[int] = Field(
        10, description='Number of players you want to retrieve, default value is 10'
    )