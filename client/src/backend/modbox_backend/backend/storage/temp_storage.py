import time

# Simple in-memory storage
TEMP_STORAGE = {}

# Default expiration in seconds (e.g., 10 minutes)
DEFAULT_EXPIRATION = 600

def set_temp(key, value, expiration=DEFAULT_EXPIRATION):
    """
    Store a value temporarily.
    """
    TEMP_STORAGE[key] = {
        "value": value,
        "expires_at": time.time() + expiration
    }

def get_temp(key):
    """
    Retrieve a temporary value if it hasn't expired.
    """
    item = TEMP_STORAGE.get(key)
    if not item:
        return None

    if time.time() > item["expires_at"]:
        del TEMP_STORAGE[key]
        return None

    return item["value"]

def delete_temp(key):
    """
    Delete a temporary value manually.
    """
    if key in TEMP_STORAGE:
        del TEMP_STORAGE[key]

def cleanup_expired():
    """
    Remove all expired items from temp storage.
    """
    now = time.time()
    expired_keys = [key for key, val in TEMP_STORAGE.items() if now > val["expires_at"]]
    for key in expired_keys:
        del TEMP_STORAGE[key]
