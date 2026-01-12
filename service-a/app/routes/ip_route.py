from fastapi import APIRouter
from models.schemas import Ip
from services.ip_service import IpManager

ip_router = APIRouter()

@ip_router.post("/ip")
def get_coordinate_by_ip(ip: Ip):
    return IpManager.get_coordinate(ip)
