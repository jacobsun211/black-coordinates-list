from fastapi import APIRouter
from app.services import get_IP_data
import requests

router = APIRouter()


@router.post('/ip')
def create_ip(ip):
    return get_IP_data(ip)


@router.post('/connection')
def send_coordinates_ip(ip_data):
    requests.post('http://service-b:8000/add_coord', json=ip_data)
    return {"status": "saved to Service B"}


