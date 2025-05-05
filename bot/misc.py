import aioredis
from aioredis import Redis

redis = aioredis.from_url("redis://host.docker.internal:6379")