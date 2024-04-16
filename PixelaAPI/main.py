import requests
from datetime import datetime

USERNAME = "your_username"
TOKEN = "password of your choice"
GRAPHID = "graph01"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# post_it = requests.post(url=pixela_endpoint, json=user_params)
# print(post_it.text)

# Creating the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post a pixel

today = datetime.now()
date = today.strftime("%Y%m%d")

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

post_pixel_config = {
    "date": date,
    "quantity": "8.5"
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(response.text)

# Put and Delete

put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"

put_config = {
    "quantity": "10.1"
}

response = requests.put(url=put_pixel_endpoint, json=put_config, headers=headers)
print(response.text)