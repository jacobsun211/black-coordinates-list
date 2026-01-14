import requests


def get_IP_data(ip):
    ip_address = ip
    url = f'http://ip-api.com/json/{ip_address}'
    response = requests.get(url).json()
    return response



