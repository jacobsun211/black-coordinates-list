from fastapi import FastAPI, APIRouter
from app.storage import get_coord, post_coord
from pydantic import BaseModel


router1 = APIRouter(tags=["server A"])
router2 = APIRouter(tags=["Redis DB"])


@router1.post("/server-b health")
def health_check():
    return {"status": "ok"}

@router2.get("/get_coord")
def get_coordinates():
    return get_coord()

    # return {"status": "ok"}

@router2.post("/add_coord")
def health(ip,coord):
    post_coord(ip, coord)
    return {"massage":"ip has been added succsefully"}
    

# @router.post("/contacts")
# def post_contact():
#     redis_db.set('half stack', 'java')



