# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:18+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Size(Enum):
    small = 'small'
    medium = 'medium'
    large = 'large'


class IdentifyBird(BaseModel):
    color: str = Field(..., description='Color of the bird.')
    habitat: str = Field(..., description='Habitat of the bird.')
    size: Optional[Size] = Field(
        Size.small, description="Size of the bird. Default is 'small'"
    )
