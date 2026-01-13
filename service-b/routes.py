from fastapi import APIRouter, Depends
import services
from schemas import Coordinate
from connection import RedisManager


router = APIRouter()

@router.get("/coordinates")
async def get_all_coordinates(conn = Depends(RedisManager.get_connection)):
    try:
        return services.get_coordinates(conn)
    except Exception as e:
        raise e
        
@router.get("/coordinates/{ip}")
async def get_coordinate_by_ip(ip: str, conn = Depends(RedisManager.get_connection)):
    try:
        return services.get_coordinate(ip, conn)
    except Exception as e:
        raise e
@router.post("/coordinates")
async def add_coordinate(coordinate: Coordinate, conn = Depends(RedisManager.get_connection)):
    try:
        return services.create_coordinate(coordinate.model_dump(), conn) 
    except Exception as e:
        raise e