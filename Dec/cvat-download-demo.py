import requests

CVAT_URL = "http://192.168.30.245:8080/projects/63?page=1"
TOKEN = "<>"

HEADERS = {
    "Authorization": f"Token {TOKEN}"
}



response = requests.get(f'{CVAT_URL}/')