from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/api/get-ip')
def get_ip():
    pass


@app.post('/api/ip')
def create_coordinates():
    pass


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
