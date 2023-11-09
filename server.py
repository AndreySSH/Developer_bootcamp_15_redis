from redis import Redis
from random import randint

with Redis() as redis_server:
    redis_server.lpush("queue", randint(0, 10))