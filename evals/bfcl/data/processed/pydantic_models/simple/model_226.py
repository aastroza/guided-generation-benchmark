# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Scale(Enum):
    percentage = 'percentage'
    field_0_10_scale = '0-10 scale'


class GetZodiacCompatibility(BaseModel):
    sign1: str = Field(..., description='The first Zodiac sign.')
    sign2: str = Field(..., description='The second Zodiac sign.')
    scale: Optional[Scale] = Field(
        Scale.percentage,
        description="The scale on which compatibility should be shown. Default is 'percentage'.",
    )