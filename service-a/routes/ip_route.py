from fastapi import APIRouter, Depends
from models.schemas import Ip
from services.ip_service import IpManager, get_ip_manager

ip_router = APIRouter()

@ip_router.post("/add-ip")
def post_coordinate(ip: Ip, ip_manager: IpManager = Depends(get_ip_manager)):
    return ip_manager.add_coordinate(ip)

@ip_router.get("/get-all-ips")
def get_all_coordinates(ip_manager: IpManager = Depends(get_ip_manager)):
    return ip_manager.get_all_coordinates()