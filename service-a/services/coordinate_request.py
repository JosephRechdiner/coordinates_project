import requests
import os

EXTERNAL_URL = os.getenv("EXTERNAL_URL")
        
def get_coordinates_from_api(ip):
    try:
        response = requests.get(EXTERNAL_URL, params=ip)
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