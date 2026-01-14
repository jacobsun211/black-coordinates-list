from fastapi import APIRouter, Request
from app.storage import get_coord, post_coord
import json


router1 = APIRouter(tags=["service A"])
router2 = APIRouter(tags=["Redis DB"])


@router1.post("/connection")
def get_ip():
    return {"status": "success"}


@router2.get("/get_coord")
def get_coordinates():
    return get_coord()


@router2.post("/add_coord")
async def add_coord(request: Request):
    data = await request.json()

    if isinstance(data, str):
        data = json.loads(data)

    ip = list(data.keys())[0]
    coord = list(data.values())[0]

    try:
        post_coord(ip, coord)
        return {"message": "ip has been added successfully"}
    except Exception as e:
        return {"error": e}
