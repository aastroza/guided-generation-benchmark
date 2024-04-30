# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:50+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Category(Enum):
    Organic = 'Organic'
    Vegetables = 'Vegetables'
    Fruits = 'Fruits'
    Dairy = 'Dairy'
    Seafood = 'Seafood'
    Bakery = 'Bakery'


class GroceryStoreFindNearby(BaseModel):
    location: str = Field(..., description='The city and state, e.g. Houston, TX')
    categories: Optional[List[Category]] = Field(
        [Category.Organic, Category.Vegetables, Category.Fruits, Category.Dairy, Category.Seafood, Category.Bakery],
        description='Categories of items to be found in the grocery store. Default is all if not specified.',
    )
