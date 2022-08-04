import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
username = 'yourusername'
token = 'yourkeyhere'

user_params = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)


graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

id = 'graph1'
graph_config = {
    'id': id,
    'name': 'Graph',
    'unit': 'Kilometers',
    'type': 'float',
    'color': 'momiji',
}
headers = {
    'X-USER-TOKEN': token
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


pixel_endpoint = f'{pixela_endpoint}/{username}/graphs/{id}'

today = datetime.now()
date = today.strftime('%Y%m%d')
pixel_config = {
    "date": date,
    "quantity": "21",
}

# response = requests.put(url=pixel_endpoint, json=pixel_config, headers=headers)


update_endpoint = f'{pixela_endpoint}/{username}/graphs/{id}/{date}'

update_config = {
    "quantity": "441",
}

# requests.put(url=update_endpoint, json=update_config, headers=headers)

requests.delete(url=update_endpoint, json=update_config, headers=headers)
