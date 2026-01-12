from fastapi import APIRouter
from models.schemas import Ip
from services.ip_service import IpManager

ip_router = APIRouter()

@ip_router.post("/ip")
def post_coordinate(ip: Ip):
    return IpManager.add_coordinate(ip)

@ip_router.get("/ip")
def get_all_coordinates():
    return IpManager.get_all_coordinates()