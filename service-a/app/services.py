import requests
import json

def get_ip():
    ip = input('get ip:\n')
    return ip


def get_IP_coordinates():
    ip_address = get_ip()
    url = f'http://ip-api.com/json/{ip_address}'
    response = requests.get(url).json()
    coordinates_data = {
        'ip': ip_address,
        'lat': response.get('lat'),
        'lon': response.get('lon')
    }
    return coordinates_data
print(get_IP_coordinates())