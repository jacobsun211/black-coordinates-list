from fastapi import APIRouter
from app.storage import get_coord, post_coord
from app.schemas import CoordRequest

router1 = APIRouter(tags=["server A"])
router2 = APIRouter(tags=["Redis DB"])


@router1.post("/connection")
def get_ip():
    return {"status": "success"}

@router2.get("/get_coord")
def get_coordinates():
    return get_coord()


@router2.post("/add_coord")
def add_coord(data: CoordRequest):
    try:
        post_coord(data.ip,data.coord)
        return {"massage":"ip has been added successfully"}
    except Exception as e:
        return {"an error occured while trying to add to Redis":e}





