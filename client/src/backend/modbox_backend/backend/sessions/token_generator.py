import secrets

TOKEN_LENGTH = 64

def generate_token():
    return secrets.token_hex(TOKEN_LENGTH // 2)
