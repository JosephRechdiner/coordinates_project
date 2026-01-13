from redis import Redis, ResponseError


async def get_coordinates(conn: Redis) -> dict:
    try:
        data = {}
        keys = conn.keys("coord:*")
        if not keys:
            return {}
        for key in keys:
            data[key] = await conn.hgetall(key)

        return {"data":data}
    except ResponseError as e:
        raise e


async def get_coordinate(ip: str, conn: Redis) -> dict:
    key = f"coord:{ip}"
    try:
        data = await conn.hgetall(key)
        if not data:
            return []
    except ResponseError as e:
        raise e


async def create_coordinate(coordinate: dict, conn: Redis):
    key = f"coord:{coordinate['ip']}"
    try:
        await conn.hset(key, mapping={"lat": coordinate["lat"], "lon": coordinate["lon"]})
        return {
            "message": "The coordinates were saved successfully",
            "coordinate": coordinate
        }
    except ResponseError as e:
        raise e 
