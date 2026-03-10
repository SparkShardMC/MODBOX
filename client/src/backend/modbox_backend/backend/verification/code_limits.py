from datetime import datetime, timedelta
from ..server.config import VERIFICATION_LIMIT_PER_HOUR, VERIFICATION_LIMIT_PER_DAY, VERIFICATION_LOCKOUT_DAYS

limit_storage = {}

def can_send_code(email):
    now = datetime.utcnow()

    record = limit_storage.get(email)

    if not record:
        limit_storage[email] = {
            "hour_count": 0,
            "day_count": 0,
            "hour_reset": now + timedelta(hours=1),
            "day_reset": now + timedelta(days=1),
            "lockout_until": None
        }
        return True

    if record["lockout_until"]:
        if now < record["lockout_until"]:
            return False
        record["lockout_until"] = None
        record["day_count"] = 0
        record["hour_count"] = 0

    if now > record["hour_reset"]:
        record["hour_count"] = 0
        record["hour_reset"] = now + timedelta(hours=1)

    if now > record["day_reset"]:
        record["day_count"] = 0
        record["day_reset"] = now + timedelta(days=1)

    if record["hour_count"] >= VERIFICATION_LIMIT_PER_HOUR:
        return False

    if record["day_count"] >= VERIFICATION_LIMIT_PER_DAY:
        record["lockout_until"] = now + timedelta(days=VERIFICATION_LOCKOUT_DAYS)
        return False

    record["hour_count"] += 1
    record["day_count"] += 1

    return True
