# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:45:58+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class SkipThrough(BaseModel):
    node: str = Field(
        ..., description='The current node being processed in the tree traversal.'
    )
    st: str = Field(
        ..., description='The state object associated with the current node.'
    )
    c: str = Field(
        ...,
        description='The callback function to be executed on the current node and state object.',
    )
