# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:41:43+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CurrentWeatherCondition(BaseModel):
    city: str = Field(
        ...,
        description='The city that you want to get the current weather conditions for.',
    )
    country: str = Field(..., description='The country of the city you specified.')
    measurement: Optional[str] = Field(
        None,
        description="You can specify which unit to display the temperature in, 'c' for Celsius, 'f' for Fahrenheit. Default is 'c'.",
    )
