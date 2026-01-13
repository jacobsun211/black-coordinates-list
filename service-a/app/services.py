import requests


def get_IP_data(ip):
    ip_address = ip
    url = f'http://ip-api.com/json/{ip_address}'
    response = requests.get(url).json()
    return get_coordinates_ip(response)


def get_coordinates_ip(response):
    coordinates_data = {
        'ip': response.get('query'),
        'lat': response.get('lat'),
        'lon': response.get('lon')
    }
    return coordinates_data
