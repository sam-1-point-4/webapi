import requests

def get_people_in_space():
    response = requests.get("http://api.open-notify.org/astros.json")
    if response.status_code == 200:
        return response.json()['people']
    return []

def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        return response.json()['iss_position']
    return {}