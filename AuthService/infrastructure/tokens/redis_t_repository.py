from use_cases.tokens.t_repo_interface import TokenRepoInterface


class RedisTokenRepository(TokenRepoInterface):
    def __init__(self, client):
        self.client = client

    async def save(self, refresh_token: str, user_id:int):
        await self.client.set(f"{user_id}", refresh_token)

    async def get(self, user_id):
        return self.client.get(f"{user_id}")

    async def delete(self, user_id):
        await self.client.delete(f"{user_id}")