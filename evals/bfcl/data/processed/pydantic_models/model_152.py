# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:41:18+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class CalculateMutualFundBalance(BaseModel):
    investment_amount: int = Field(
        ..., description='The initial total amount invested in the fund.'
    )
    annual_yield: float = Field(
        ...,
        description='The annual yield rate of the fund. This is a float type value.',
    )
    years: int = Field(..., description='The period of time for the fund to mature.')
