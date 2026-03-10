from datetime import datetime, timedelta
from ..server.config import VERIFICATION_CODE_EXPIRATION
from .code_generator import generate_code

verification_storage = {}

def create_code(email):
    code = generate_code()
    expires = datetime.utcnow() + timedelta(seconds=VERIFICATION_CODE_EXPIRATION)

    verification_storage[email] = {
        "code": code,
        "expires": expires,
        "attempts": 0
    }

    return code

def verify_code(email, user_code):
    record = verification_storage.get(email)

    if not record:
        return False

    if datetime.utcnow() > record["expires"]:
        del verification_storage[email]
        return False

    if record["code"] != user_code:
        record["attempts"] += 1
        return False

    del verification_storage[email]
    return True
