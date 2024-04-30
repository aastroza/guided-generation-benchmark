# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:37+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GetTheaterMovieReleases(BaseModel):
    location: str = Field(..., description='The location of the theaters.')
    timeframe: int = Field(
        ...,
        description='The number of days for which releases are required from current date.',
    )
    format: Optional[str] = Field(
        'all',
        description="Format of movies - could be 'IMAX', '2D', '3D', '4DX' etc. Default is 'all'",
    )
