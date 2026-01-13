from redis import Redis
from fastapi import HTTPException, status

def get_coordinates(conn: Redis) -> dict:
    try:
        keys = conn.keys("coord:*")
        if not keys:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="There are no coordinates in data."
            )
        data = {}
        for key in keys:
            data[key] = conn.hgetall(key)
        
        return data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )
    finally:
        conn.close()

def get_coordinate(ip: str, conn: Redis) -> dict:
    key = f"coord:{ip}"
    try:
        data = conn.hgetall(key)
        if not data:
            raise HTTPException(status_code=404, detail="IP address not found")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        conn.close()

def create_coordinate(coordinate: dict, conn: Redis):
    key = f"coord:{coordinate['ip']}"
    try:
        conn.hset(key, mapping={"lat": coordinate["lat"], "lon": coordinate["lon"]})
        return {"message": "The coordinates were saved successfully."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Saving to the database failed."
        )
    finally:
        conn.close()