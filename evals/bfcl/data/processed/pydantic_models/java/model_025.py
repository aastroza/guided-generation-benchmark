# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:30+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class SmshomerecommendsubjectcontrollerUpdatesort(BaseModel):
    id: int = Field(
        ..., description='The unique identifier of the recommended subject to update.'
    )
    sort: int = Field(
        ..., description='The new sort order value for the recommended subject.'
    )