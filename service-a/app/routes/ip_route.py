from fastapi import APIRouter
from models.schemas import Ip
from services.ip_service import IpManger

ip_router = APIRouter()

@ip_router.post("/ip")
def get_coordinate(ip: Ip):
    return IpManger.get_coordinate(ip)
