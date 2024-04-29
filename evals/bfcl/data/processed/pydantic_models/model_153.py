# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:41:19+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class CalculateCompoundedInterest(BaseModel):
    principal: int = Field(
        ..., description='The initial amount of money that is being invested or loaned.'
    )
    rate: float = Field(
        ..., description='The annual interest rate. This is a float type value.'
    )
    time: int = Field(
        ...,
        description='The number of time periods the money is invested or loaned for.',
    )
    n: int = Field(
        ...,
        description='The number of times that interest is compounded per unit time.',
    )
