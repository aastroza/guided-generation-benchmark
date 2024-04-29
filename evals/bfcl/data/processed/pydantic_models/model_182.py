# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:41:40+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class LawsuitInfo(BaseModel):
    case_number: str = Field(
        ..., description='The unique identifier of the lawsuit case'
    )
    year: Optional[int] = Field(
        None,
        description='The year in which the lawsuit case was initiated. Default is latest year if not specified.',
    )
    location: Optional[str] = Field(
        None,
        description="The location or court jurisdiction where the case was filed. Default is 'all'.",
    )
