# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:43:51+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GetBestSushiPlaces(BaseModel):
    city: str = Field(
        ..., description='The city in which to look for the sushi places.'
    )
    top: int = Field(..., description='The number of top sushi places to be returned.')
    review_rate: Optional[float] = Field(
        None,
        description='The review rating to filter the sushi places. Places with review ratings above this value will be returned. Default 0.00. This is a float type value.',
    )
