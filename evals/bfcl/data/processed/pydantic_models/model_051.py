# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:44:54+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class CcrusagetransportactionMasteroperation(BaseModel):
    task: str = Field(..., description='The task associated with the request.')
    request: str = Field(
        ..., description='The XPackUsageRequest object containing the request details.'
    )
    state: str = Field(..., description='The current cluster state.')
    listener: str = Field(
        ...,
        description='The ActionListener that handles the response containing the usage statistics.',
    )
