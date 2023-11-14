from .models import Token
from uuid import uuid4

class TokenClass:
    @classmethod
    def create_token(tok):
        rand_token = uuid4()
        if tok.check_token(user_token=rand_token):
            Token.objects.create(token=rand_token)
            return rand_token

    @staticmethod
    def check_token(user_token: str):
        tokens = Token.objects.filter(token=user_token)
        if len(tokens.values()):
            return False
        else:
            return True