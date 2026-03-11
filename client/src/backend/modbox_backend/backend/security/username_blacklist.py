BLACKLIST = {
    "admin",
    "administrator",
    "mod",
    "moderator",
    "staff",
    "owner",
    "system",
    "support",
    "modbox",
    "root"
}

def is_username_allowed(username):
    lowered = username.lower()

    if lowered in BLACKLIST:
        return False

    return True
