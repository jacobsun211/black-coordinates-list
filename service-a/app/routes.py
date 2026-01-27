from fastapi import APIRouter
from app.services import get_IP_data
import requests

router = APIRouter()

def get_coordinates_ip(response):
    ip = response.get('query')
    coord = f'{response.get("lat")}, {response.get("lon")}'

    requests.post('http://localhost:8000/add_coord',
                  params={'ip': ip, 'coord': coord})

    return send_coordinates_ip({ip: coord})

@router.post('/ip')
def create_ip(ip):
    coord = get_IP_data(ip)
    return get_coordinates_ip(coord)


@router.post('/connection')
def send_coordinates_ip(ip_data):
    requests.post('http://service-b:8000/add_coord', json=ip_data)
    return {"status": "saved to Service B"}


