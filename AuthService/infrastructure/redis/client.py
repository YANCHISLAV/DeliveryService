from redis.asyncio import Redis as AsyncRedis, ConnectionPool


class Redis:
    def __init__(self,
            host: str,
            port: int,
            db: int,
            password: str,
            max_connections: int
        ):
        self.pool = ConnectionPool(
            host=host,
            port=port,
            db=db,
            password=password,
            max_connections=max_connections,
            decode_responses=True
        )
        self.client = AsyncRedis(connection_pool=self.pool)

    async def close(self):
        await self.client.close()

    async def get_client(self) -> AsyncRedis:
        return self.client
