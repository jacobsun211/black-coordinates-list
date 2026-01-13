from fastapi import APIRouter
from services import get_IP_data
from schemas import IPRequest, IPResponse



router = APIRouter()


@router.post('/ip')
def create_ip(ip):
    return get_IP_data(ip)


@router.post('/connection')
def send_coordinates_ip(ip_data):
    return