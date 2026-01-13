from fastapi import FastAPI, APIRouter
import redis
import uvicorn
from pydantic import BaseModel


router1 = APIRouter(tags=["server A"])
router2 = APIRouter(tags=["Redis DB"])


@router1.get("/server-b health")
def health_check():
    return {"status": "ok"}

@router2.get("/redis health")
def health():
    return {"status": "ok"}
    

# @router.post("/contacts")
# def post_contact():
#     redis_db.set('half stack', 'java')



