import requests


def get_IP_data(ip):
    ip_address = ip
    url = f'http://ip-api.com/json/{ip_address}'
    response = requests.get(url).json()
    return get_coordinates_ip(response)


def get_coordinates_ip(response):
    ip = response.get('query')
    coord = f'{response.get("lat")}, {response.get("lon")}'

    requests.post('http://localhost:8000/add_coord', 
        params={'ip': ip, 'coord': coord})  

    return {ip: coord}
