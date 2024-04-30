# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:16+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Region(Enum):
    Northern = 'Northern'
    Southern = 'Southern'
    Eastern = 'Eastern'
    Western = 'Western'


class Category(Enum):
    Wars = 'Wars'
    Culture = 'Culture'
    Politics = 'Politics'
    Scientific = 'Scientific'
    Others = 'Others'


class HistoryEuFetchEvents(BaseModel):
    century: int = Field(..., description='The century you are interested in.')
    region: Region = Field(
        ..., description='The region of Europe you are interested in.'
    )
    category: Optional[Category] = Field(
        Category.Culture, description="Category of the historical events. Default is 'Culture'."
    )
