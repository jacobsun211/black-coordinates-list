from fastapi import FastAPI
from routes import router
import routes
import uvicorn


app = FastAPI()
app.include_router(routes.router)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
