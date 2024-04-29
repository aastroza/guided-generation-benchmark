# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:40:56+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ChiSquaredTest(BaseModel):
    table: List[int] = Field(
        ..., description='A 2x2 contingency table presented in array form.'
    )
    alpha: Optional[float] = Field(
        None,
        description='Significance level for the Chi-Squared test. Default is 0.05. This is a float type value.',
    )
