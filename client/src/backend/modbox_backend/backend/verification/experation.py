from datetime import datetime
from .verification_codes import verification_storage

def clear_expired():
    now = datetime.utcnow()
    expired = []

    for email, record in verification_storage.items():
        if now > record["expires"]:
            expired.append(email)

    for email in expired:
        del verification_storage[email]
