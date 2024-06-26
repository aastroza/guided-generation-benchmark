# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:00+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class LinearRegressionGetRSquared(BaseModel):
    dataset_path: str = Field(..., description='Path to the CSV dataset file.')
    independent_variables: List[str] = Field(
        ..., description='The independent variables to use in the regression model.'
    )
    dependent_variable: str = Field(
        ..., description='The dependent variable to predict in the regression model.'
    )
