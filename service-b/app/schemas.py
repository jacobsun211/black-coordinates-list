from pydantic import BaseModel

class CoordRequest(BaseModel):
    ip: str
    coord: str
