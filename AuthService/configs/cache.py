from pydantic import BaseModel


class CacheConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 6379
    db: int = 0
    password: str
    max_connections: int = 50