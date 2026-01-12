import requests
from fastapi import HTTPException

API_URL = "http://ip-api.com/json"

def get_coordinate(ip):
    response = requests.get(API_URL, params=ip)
    if not response.status_code == 200:
        raise HTTPException(status_code=404, detail="No coordinate found for this Ip!")
    data = response.json()
    return {
        "ip": ip,
        "lat": data["lat"],
        "lon": data["lon"]
    }
