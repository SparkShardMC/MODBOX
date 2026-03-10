import re
from ..server.config import MIN_PASSWORD_LENGTH

def validate_password(password):
    if len(password) < MIN_PASSWORD_LENGTH:
        return False, "Password must be at least 10 characters"

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain an uppercase letter"

    if not re.search(r"[0-9]", password):
        return False, "Password must contain a number"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain a special character"

    return True, None
