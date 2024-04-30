# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:36+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GameScoreHighest(BaseModel):
    game: str = Field(..., description='The name of the online game.')
    platform: str = Field(
        ...,
        description='The platform where the game is played, e.g. PC, Xbox, Playstation',
    )
    region: Optional[str] = Field(
        'Global', description="The geographic region of the player. Defaults to 'Global'"
    )
