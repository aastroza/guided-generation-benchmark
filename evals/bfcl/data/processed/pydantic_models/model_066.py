# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:45:04+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class CompositeruntimefieldCreatechildruntimefield(BaseModel):
    parserContext: str = Field(
        ..., description='The context used for parsing the mapping.'
    )
    parent: str = Field(..., description='The name of the parent field.')
    parentScriptFactory: str = Field(
        ...,
        description='A factory function to create a script for the parent composite field.',
    )
    onScriptError: str = Field(
        ..., description='The strategy for handling script errors.'
    )
