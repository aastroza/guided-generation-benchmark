# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:32+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class LegalCaseFetch(BaseModel):
    case_id: str = Field(..., description='The ID of the legal case.')
    details: bool = Field(..., description='True if need the detail info. ')
