# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:41:33+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class LawCaseSearch(BaseModel):
    topic: str = Field(..., description='The subject matter of the case.')
    year_range: List[int] = Field(
        ..., description='The start and end year for searching cases.'
    )
    location: str = Field(
        ..., description='The location where the case is being heard.'
    )
    judicial_system: Optional[str] = Field(
        'all',
        description="The specific judicial system in which to search (e.g. 'federal', 'state').",
    )
