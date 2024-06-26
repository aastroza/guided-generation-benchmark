# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ElectromagneticForce(BaseModel):
    charge1: int = Field(
        ..., description='The magnitude of the first charge in coulombs.'
    )
    charge2: int = Field(
        ..., description='The magnitude of the second charge in coulombs.'
    )
    distance: int = Field(
        ..., description='The distance between the two charges in meters.'
    )
    medium_permittivity: Optional[float] = Field(
        8.854e-12,
        description='The relative permittivity of the medium in which the charges are present. Default is 8.854e-12 (Vacuum Permittivity). This is a float type value.',
    )
