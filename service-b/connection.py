import redis
import os

class RedisManager:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            host = os.getenv('REDIS_HOST')
            port = int(os.getenv('REDIS_PORT'))

            try:
                pool = redis.ConnectionPool(
                    host=host, 
                    port=port, 
                    decode_responses=True,
                    socket_timeout=5 
                )
                cls._connection = redis.Redis(connection_pool=pool)
                
                cls._connection.ping()
            except redis.ConnectionError as e:
                print(f"Error connecting to Redis: {e}")
                raise
        
        return cls._connection