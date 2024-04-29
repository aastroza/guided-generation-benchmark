# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:41:38+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class LawsuitsSearch(BaseModel):
    company_name: str = Field(..., description='The name of the company.')
    location: str = Field(..., description='The location where the lawsuit was filed.')
    year: int = Field(..., description='The year when the lawsuit was filed.')
    case_type: Optional[str] = Field(
        None,
        description="The type of the case. Options include: 'civil', 'criminal', 'small_claims', etc. Default is 'all'.",
    )
