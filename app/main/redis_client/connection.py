from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv
from functools import lru_cache
import config
from fastapi import Depends


@lru_cache()
def get_settings():
    return config.Settings()


def connection_redis(settings: config.Settings = Depends(get_settings)):
    try:
        redis_client = Redis(
            host="redis", # settings.redis_host   This 3 for connection with redis service
            port=6379 # settings.redis_port
            # password=settings.redis_password
        )
        return redis_client
    except ConnectionError as e:
        print(e)
