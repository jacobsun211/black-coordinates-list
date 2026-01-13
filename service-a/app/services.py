import requests
import json


def get_ip():
    ip = input('get ip:\n')
    return ip


def get_IP_coordinates():
    ip_address = get_ip()
    url = f'http://ip-api.com/json/{ip_address}'
    response = requests.get(url).json()
    coordinates = []
    coordinates.append(response.get('lat'))
    coordinates.append(response.get('lon'))
    coordinates_data = {
        ip_address: coordinates
    }
    return coordinates_data
