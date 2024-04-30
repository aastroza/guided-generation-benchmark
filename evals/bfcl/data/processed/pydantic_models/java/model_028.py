# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:32+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class ConfigstorageDynamiccredentialsscheduledexecutorservice(BaseModel):
    credentialsFile: str = Field(..., description='The path to the credentials file.')
    credentialsRefreshInterval: int = Field(
        ...,
        description='The interval in seconds at which the credentials file should be reloaded.',
    )
    basicCredentials: str = Field(
        ...,
        description='The BasicCredentials object containing the current credentials.',
    )