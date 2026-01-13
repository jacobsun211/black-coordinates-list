from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from app.routes import router1 as endpoints
from app.routes import router2 as redis



app = FastAPI(
    title="SERVER B",
    version="1.0.0"
)


app.include_router(endpoints) 
app.include_router(redis) 



# class Contact_params(BaseModel):
#     first_name: str
#     last_name: str
#     phone_number: str
