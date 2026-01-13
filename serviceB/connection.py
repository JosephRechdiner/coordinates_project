import redis
import os

class RedisManager:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            host = os.getenv('REDIS_HOST', 'localhost')
            port = int(os.getenv('REDIS_PORT', 6379))
            password = os.getenv('REDIS_PASSWORD', None)

            try:
                pool = redis.ConnectionPool(
                    host=host, 
                    port=port, 
                    password=password,
                    decode_responses=True,
                    socket_timeout=5 
                )
                cls._connection = redis.Redis(connection_pool=pool)
                
                cls._connection.ping()
            except redis.ConnectionError as e:
                print(f"Error connecting to Redis: {e}")
                raise
        
        return cls._connection