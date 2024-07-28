# HTTP request

import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "username"
TOKEN = "token"
graphid = "graph-01"

users_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)
# output: {"message":"Success. Let's visit https://pixe.la/@monty001 , it is your profile page!","isSuccess":true}

# after getting the output comment the rsponse

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id":"graph-01",
    "name":"Running graph",
    "unit":"Km",
    "type":"float",
    "color":"sora"
}

# This is the authentication header which secure your sensitive info from others
headers = {
    'X-USER-TOKEN':TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# To check the dashboard
# https://pixe.la/v1/users/monty001/graphs/graph-01.html

# today = datetime.now()

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphid}"

today = datetime(year=2024, month=7, day=28)

pixela_data = {
    # "date": "20240728",
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today?  "),
}

response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=headers)
print(response.text)

# pixela_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphid}/{today.strftime('%Y%m%d')}"
#
# new_pixela_data = {
#     "quantity": "10",
# }
# response = requests.put(url=pixela_update_endpoint, json=new_pixela_data, headers=headers)
# print(response.text)

# pixela_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphid}/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(url=pixela_delete_endpoint, headers=headers)
# print(response.text)
