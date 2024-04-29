# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:43:57+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class WholeFoodsCheckPrice(BaseModel):
    location: str = Field(..., description='Location of the Whole Foods store.')
    items: List[str] = Field(
        ..., description='List of items for which the price needs to be checked.'
    )
