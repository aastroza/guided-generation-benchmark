# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:16+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class PlaintextpresentationCreatepresentation(BaseModel):
    controller: str = Field(
        ...,
        description='The IResultSetController instance responsible for managing the result set.',
    )
    parent: str = Field(
        ...,
        description='The Composite UI element that will contain the plain text presentation.',
    )
