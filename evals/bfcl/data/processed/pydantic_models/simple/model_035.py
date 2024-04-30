# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:56+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class VeganRestaurantFindNearby(BaseModel):
    location: str = Field(
        ...,
        description='The city and state, e.g. New York, NY, you should format it as City, State.',
    )
    operating_hours: Optional[int] = Field(
        24,
        description='Preferred latest closing time of the restaurant. E.g. if 11 is given, then restaurants that close at or after 11 PM will be considered. This is in 24 hour format. Default is 24.',
    )
