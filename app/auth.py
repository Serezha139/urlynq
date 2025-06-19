from flask_httpauth import HTTPTokenAuth
from settings import TOKEN_LIST

auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    if token in TOKEN_LIST:
        return TOKEN_LIST[token]
