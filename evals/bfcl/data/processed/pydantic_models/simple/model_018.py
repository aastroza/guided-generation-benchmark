# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:44+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class NumberAnalysisPrimeFactors(BaseModel):
    number: int = Field(..., description='The number to be factored.')
