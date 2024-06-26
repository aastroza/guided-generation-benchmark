# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:53+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class InvokeCallback(BaseModel):
    callback: str = Field(..., description='The callback function to be invoked.')
    error: str = Field(
        ...,
        description="The error to pass to the callback function. Can be 'null' if there is no error.",
    )
    value: str = Field(..., description='The value to pass to the callback function.')
