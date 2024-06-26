# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:35+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class GetRestaurant(BaseModel):
    cuisine: str = Field(..., description='Cuisine of the restaurant.')
    location: str = Field(..., description='City where restaurant is located.')
    condition: str = Field(
        ...,
        description='Condition to be met by the restaurant (e.g., operating days, amenities, etc.)',
    )
