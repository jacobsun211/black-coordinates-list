from pydantic import BaseModel


class IPRequest(BaseModel):
    ip: str


class IPResponse(BaseModel):
    ip: str
    lat: float
    lon: float
