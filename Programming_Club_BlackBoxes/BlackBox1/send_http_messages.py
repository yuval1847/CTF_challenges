import requests
import base64_decrypter

# def check_right_hash():
#     # The function gets nothing.
#     # The function bruteforce all the 2019 dates and find the right hash of the admin user.
#     # The function returns the hash which fits to the date.
#     URL = "http://localhost:5555"
#     message_body = {"action": "login", "username": "admin", "token": "Y3liZXI=", "hash": ""}
#     current_date = ""
#     for current_month in range(1, 13):
#         for current_day in range(1, 31):
#             current_date = str(current_day)+"/"+str(current_month)+"/2019"
#             message_body["hash"] = base64_decrypter.generate_sha1_hash(current_date)
#             respond = requests.post(url=URL, json=message_body)
#             # respond_data = respond.json()
#             if respond.status_code == 200:
#                 print("success - " + current_date + " - " + message_body["hash"])
#                 return message_body["hash"]
#             print("fail - " + current_date + " - " + message_body["hash"])
            
# print(check_right_hash())

URL = "http://localhost:5555"

# Login request
message_body = {"action": "login", "username": "admin", "token": "Y3liZXI=", "hash": "b1f38bb02297db3a5ca9324b3089fd73459d60b9"}
# Get-actions request
#message_body = {"action": "get-actions", "type": "admin", "token": "Y3liZXI="}
# Get-users request
#message_body = {"action": "get-users", "type": "admin", "token": "Y3liZXI="}

respond = requests.post(url=URL, json=message_body)
respond_data = respond.json()
if respond.status_code == 200:
    print(respond_data)
else:
    print(f"Error{respond.status_code}")