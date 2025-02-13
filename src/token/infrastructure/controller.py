from src.token.infrastructure.mongod import MongodToken
from ..application.response import TokenResponse

class TokenController:

    def __init__(self):
        self.mongo_token = MongodToken()
        self.response = TokenResponse()

    def authenticate_token(self, token):
        token_info = self.mongo_token.TokenConnect(token)
        parsed = self.response.parsedToken(token_info)
        return parsed


