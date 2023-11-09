from redis import Redis

with Redis() as redis_client:
    value = redis_client.brpop("queue")

print(int(value[1]))