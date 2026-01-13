from fastapi import FastAPI
from app.routes import router1 as endpoints
from app.routes import router2 as redis

app = FastAPI(
    title="service B",
    version="1.0.0"
)

app.include_router(endpoints)
app.include_router(redis)
