# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:21+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class SportsTeamGetSchedule(BaseModel):
    team_name: str = Field(..., description='The name of the sports team.')
    num_of_games: int = Field(
        ..., description='Number of games for which to fetch the schedule.'
    )
    league: str = Field(
        ...,
        description='The name of the sports league. If not provided, the function will fetch the schedule for all games, regardless of the league.',
    )
    location: Optional[str] = Field(
        'all',
        description='Optional. The city or venue where games are to be held. If not provided, default that all venues will be considered.',
    )
