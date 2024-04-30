# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:55+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class RestaurantFindNearby(BaseModel):
    location: str = Field(..., description='The city and state, e.g. Seattle, WA')
    cuisine: str = Field(..., description='Preferred type of cuisine in restaurant.')
    max_distance: Optional[int] = Field(
        5,
        description='Maximum distance (in miles) within which to search for restaurants. Default is 5.',
    )
