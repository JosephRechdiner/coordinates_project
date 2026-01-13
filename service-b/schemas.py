from pydantic import BaseModel, Field
from typing import Optional


class Coordinate(BaseModel):
    ip: str
    lat: float =Field(ge=-90, le= 90)
    lon: float =Field(ge=-180, le= 180)