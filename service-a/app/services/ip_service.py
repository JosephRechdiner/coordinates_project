from coordinate_request import get_coordinates_api
from fastapi import HTTPException
import requests
import os

DEST_URL = os.getenv("SERVER_B_URL")

class IpManager:
    @staticmethod
    def get_coordinate(ip):
        try:
            coordinates = get_coordinates_api(ip)
            if not coordinates:
                raise HTTPException(status_code=404, detail="No coordinates found for this Ip!")
            response = requests.post(DEST_URL, json=coordinates)
            if not response.status_code == 200:
                raise HTTPException(status_code=404, detail="No server found for inserting data!")
            return coordinates
        except Exception as e:
            print(f"Error: {e}")