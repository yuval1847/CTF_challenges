import requests
URL = "http://127.0.0.1"
PARAMS = {"action": "login", "username": "abcd", "token": "MTIzNA==", "hash": "72cd726f3b6b5a705bf9e9461a8986be2451fad4"}
respond = requests.get(url=URL, params=PARAMS)
respond_data = respond.json()
print(respond_data)