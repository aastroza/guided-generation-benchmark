# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:43:38+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class GetGameItemStats(BaseModel):
    game: str = Field(..., description='The game to retrieve information from.')
    item: str = Field(..., description='The name of the item in the game.')
    stat: str = Field(..., description='Specific statistic required.')
