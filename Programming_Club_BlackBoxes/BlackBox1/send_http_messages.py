import requests
URL = "http://localhost:5555"
# Login request
#message_body = {"action": "login", "username": "abcd", "token": "MTIzNA==", "hash": "6dccd157d0d32c6f462c52c99247a3a06999f146"}
# Get-actions request
#message_body = {"action": "get-actions", "type": "admin", "token": "MTIzNA=="}
# Get-users request
message_body = {"action": "get-users", "type": "admin", "token": "MTIzNA=="}

respond = requests.post(url=URL, json=message_body)
respond_data = respond.json()
if respond.status_code == 200:
    print(respond_data)
else:
    print(f"Error{respond.status_code}")