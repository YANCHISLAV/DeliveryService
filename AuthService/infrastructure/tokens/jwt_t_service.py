from datetime import datetime, timedelta

from configs.settings import get_settings
import jwt

from use_cases.tokens.t_service_interface import TokenServiceInterface


class JWTTokenService(TokenServiceInterface):
    def __init__(self, token_repo):
        self.token_repo = token_repo

    async def create(self, user_id: int)->dict:
        time = datetime.now()
        access_token = jwt.encode({'user_id': user_id, "token_type":"access_token",
                                   "iat": time, "exp": time+timedelta(minutes=15)},
                                  key=get_settings().auth.secret_key,
                                  algorithm=get_settings().auth.algorithm
                                  )

        refresh_token = jwt.encode({'user_id': user_id, "token_type":"refresh_token",
                                   "iat": time.timestamp(), "exp": (time+timedelta(weeks=1)).timestamp()},
                                  key=get_settings().auth.secret_key,
                                  algorithm=get_settings().auth.algorithm
                                  )
        await self.token_repo.save(refresh_token, user_id)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'token_type': 'bearer'
        }

    async def update(self, user_id)->dict:

        refresh_token = await self.token_repo.get(user_id)
        try:
            jwt.decode(refresh_token,
                       key=get_settings().auth.secret_key,
                       algorithm=get_settings().auth.algorithm
                       )
        except jwt.ExpiredSignatureError:
            await self.token_repo.delete(user_id)
            tokens = await self.create(user_id)
            return tokens
        time = datetime.now()
        access_token = jwt.encode({'user_id': user_id, "token_type": "access_token",
                                   "iat": time.timestamp(), "exp": (time + timedelta(minutes=15)).timestamp()},
                                    key=get_settings().auth.secret_key,
                                    algorithm=get_settings().auth.algorithm
                                    )
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'token_type': 'bearer'
        }

    async def delete(self, user_id):
        await self.token_repo.delete(user_id)
