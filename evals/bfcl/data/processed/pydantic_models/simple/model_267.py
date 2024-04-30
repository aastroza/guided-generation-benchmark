# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:39+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class UserRatings(Enum):
    low = 'low'
    average = 'average'
    high = 'high'


class FindExhibition(BaseModel):
    location: str = Field(
        ...,
        description='The city where the exhibition is held, e.g., New York City, NY.',
    )
    art_form: str = Field(
        ..., description='The form of art the exhibition is displaying e.g., sculpture.'
    )
    month: Optional[str] = Field(
        'upcoming',
        description='The month of exhibition. Default value will return upcoming events if not specified.',
    )
    user_ratings: Optional[UserRatings] = Field(
        UserRatings.low,
        description="Select exhibitions with user rating threshold. Default is 'low'",
    )
