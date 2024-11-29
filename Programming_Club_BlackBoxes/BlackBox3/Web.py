# Web:
import requests

def get_respond(url:str, params:dict):
    # The function gets url and parameters.
    # The function returns the respond from the server.
    respond = requests.get(url=url, params=params)
    if respond.status_code == 200:
        return respond
    return None

respond = get_respond("http://google.com:8080/", params={})
print(respond.json)