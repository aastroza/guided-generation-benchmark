# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:43:47+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GetRecipe(BaseModel):
    dish_name: str = Field(
        ..., description='Name of the dish whose recipe needs to be fetched.'
    )
    diet_preference: Optional[str] = Field(
        'none',
        description='Preferred dietary consideration like vegan, vegetarian, gluten-free etc. Default is none.',
    )
