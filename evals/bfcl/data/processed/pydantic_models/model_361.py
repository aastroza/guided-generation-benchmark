# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:43:50+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class RestaurantFinder(BaseModel):
    city: str = Field(..., description='City where you are looking for the restaurant.')
    cuisine: str = Field(..., description='Type of cuisine you are interested in.')
    diet: Optional[str] = Field(
        None,
        description="Dietary preferences. e.g. 'Vegetarian', 'Gluten-free', etc. Default 'Vegetarian'.",
    )
