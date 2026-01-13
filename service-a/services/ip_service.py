from .coordinate_request import get_coordinates_from_api
from fastapi import HTTPException
from requests import Session
import os

INTERNAL_URL = os.getenv("INTERNAL_URL")

class IpManager:
    def __init__(self):
        self.session = Session()
        
    def add_coordinate(self, ip):
        try:
            coordinates = get_coordinates_from_api(str(ip.ip))
            if not coordinates:
                raise HTTPException(status_code=404, detail="No coordinates found for this Ip!")
            response = self.session.post(INTERNAL_URL, json=coordinates)
            if not response.status_code == 200:
                raise HTTPException(status_code=response.status_code, detail="No server found for inserting data!")
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
    
    def get_all_coordinates(self):
        try:
            response = self.session.get(INTERNAL_URL)
            if not response.status_code == 200:
                raise HTTPException(status_code=response.status_code, detail="No server found for getting data!")
            return response.json()
        except Exception as e:
            print(f"Error: {e}")

def get_ip_manager():
    ip_manager = IpManager()
    return ip_manager