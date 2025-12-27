import requests
from datetime import datetime
import os

USERNAME = "ochuba"
TOKEN = os.getenv("TOKEN")
ID = "graph1001"

QUANTITY = input("how many minutes did you code today?")



PIXELA_END_POINT = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# --------- TO CREATE A USER ----------------- #
# response = requests.post(PIXELA_END_POINT, json=user_parameters)
# responses = response.text
# print(responses)

# --------------- GRAPH CREATION ------------------ #

graph_parameters = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "mins",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# graph_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs"
# response = requests.post(graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)


# -------- POST TO THE GRAPH ---------------- #

today = datetime.now()
TODAY = today.strftime("%Y%m%d")

graph_post_parameters = {
    "date": TODAY,
    "quantity": QUANTITY,
}

# graph_post_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs/{ID}"
# response = requests.post(graph_post_endpoint, json=graph_post_parameters, headers=headers)
# print(response.text)

# ---------------- UPDATE  POST --------------- #

graph_update_parameters = {
    "quantity": QUANTITY,
}

graph_update_endpoint = f" {PIXELA_END_POINT}/{USERNAME}/graphs/{ID}/{TODAY}"
response = requests.put(graph_update_endpoint, headers=headers, json=graph_update_parameters)
print(response.text)

# -------------------- DELETE POST -------------------- #

# graph_delete_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs/{ID}/{TODAY}"
# response = requests.delete(graph_delete_endpoint, headers=headers)
# print(response.text)
