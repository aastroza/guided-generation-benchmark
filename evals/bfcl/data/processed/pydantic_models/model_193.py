# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:41:48+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class PlantType(Enum):
    Annual = 'Annual'
    Perennial = 'Perennial'
    Shrub = 'Shrub'
    Tree = 'Tree'
    Herbs = 'Herbs'
    Fruits = 'Fruits'


class LocalNurseryFind(BaseModel):
    location: str = Field(
        ..., description='The city or locality where the nursery needs to be located.'
    )
    plant_types: List[PlantType] = Field(
        ..., description='Type of plants the nursery should provide.'
    )
