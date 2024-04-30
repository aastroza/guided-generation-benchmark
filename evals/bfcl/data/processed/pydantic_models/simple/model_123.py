# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:58+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class HypothesisTestingTwoSampleTTest(BaseModel):
    group1: List[float] = Field(..., description='Sample observations from group 1.')
    group2: List[float] = Field(..., description='Sample observations from group 2.')
    alpha: Optional[float] = Field(
        0.05,
        description='Significance level for the t-test. Default is 0.05. This is a float type value.',
    )