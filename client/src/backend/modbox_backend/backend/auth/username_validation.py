from ..server.config import USERNAME_MIN_LENGTH, USERNAME_MAX_LENGTH

reserved_usernames = {
    "admin",
    "root",
    "system",
    "modbox",
    "support",
    "api"
}

existing_usernames = set()

def validate_username(username):
    if len(username) < USERNAME_MIN_LENGTH:
        return False, "Username too short"

    if len(username) > USERNAME_MAX_LENGTH:
        return False, "Username too long"

    if username.lower() in reserved_usernames:
        return False, "Username is restricted"

    if username in existing_usernames:
        return False, "Username already taken"

    return True, None
