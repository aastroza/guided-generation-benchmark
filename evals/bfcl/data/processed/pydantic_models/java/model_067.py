# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:00+00:00

from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel, Field


class MacdmgbundlerPreparedmgsetupscript(BaseModel):
    appLocation: str = Field(
        ..., description='The file system path string to the application location.'
    )
    params: Dict[str, Any] = Field(
        ...,
        description='A map of parameters that may include the application name, images root, background image folder, and other packaging parameters.',
    )