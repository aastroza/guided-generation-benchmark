# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:57+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class WithinQuery(BaseModel):
    field: str = Field(..., description='The name of the field to query.')
    from_: int = Field(
        ..., alias='from', description='The lower bound of the range query.'
    )
    to: int = Field(..., description='The upper bound of the range query.')
    includeFrom: bool = Field(
        ..., description="Whether to include the 'from' value in the range."
    )
    includeTo: bool = Field(
        ..., description="Whether to include the 'to' value in the range."
    )
