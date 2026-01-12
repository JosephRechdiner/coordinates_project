import requests
import os

API_URL = "http://ip-api.com/json"
        
def get_coordinates_api(ip):
    try:
        response = requests.get(API_URL, params=ip)
        if not response.status_code == 200:
            return False
        data = response.json()
        return {
            "ip": ip,
            "lat": data["lat"],
            "lon": data["lon"]
        }
    except Exception as e:
        print(f"Error getting the coordinates {e}")