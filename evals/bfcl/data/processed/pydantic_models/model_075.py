# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:45:10+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class JdkxmlfeaturesGetsystemproperty(BaseModel):
    feature: str = Field(
        ..., description='The XML feature to check the system property for.'
    )
    sysPropertyName: str = Field(
        ..., description='The name of the system property to be checked.'
    )
