from coordinate_request import get_coordinates_api
from fastapi import HTTPException
import requests
import os

INTERNAL_URL = os.getenv("INTERNAL_URL")

class IpManager:
    @staticmethod
    def add_coordinate(ip):
        try:
            coordinates = get_coordinates_api(ip)
            if not coordinates:
                raise HTTPException(status_code=404, detail="No coordinates found for this Ip!")
            response = requests.post(INTERNAL_URL, json=coordinates)
            if not response.status_code == 200:
                raise HTTPException(status_code=404, detail="No server found for inserting data!")
            return coordinates
        except Exception as e:
            print(f"Error: {e}")
    
    @staticmethod
    def get_all_coordinates():
        try:
            response = requests.get(INTERNAL_URL)
            if not response.status_code == 200:
                raise HTTPException(status_code=404, detail="No server found for getting data!")
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
