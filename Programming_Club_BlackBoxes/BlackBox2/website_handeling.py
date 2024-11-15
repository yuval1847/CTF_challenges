import requests

URL = "http://localhost:5000"

message_body = {}
respond = requests.post(url=URL, json=message_body)
respond_data = respond.json()
if respond.status_code == 200:
    print(respond_data)
else:
    print(f"Error {respond.status_code}")