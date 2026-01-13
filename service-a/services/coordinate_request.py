import requests
import os
from fastapi import HTTPException

EXTERNAL_URL = os.getenv("EXTERNAL_URL")
        
def get_coordinates_from_api(ip):
    try:
        full_path = f"{EXTERNAL_URL}/{ip}"
        response = requests.get(full_path)
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
        raise HTTPException(status_code=404, detail=str(e))