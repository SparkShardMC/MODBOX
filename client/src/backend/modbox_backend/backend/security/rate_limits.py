import time

REQUEST_LOG = {}

RATE_LIMIT_WINDOW = 60
MAX_REQUESTS = 10

def is_rate_limited(identifier):
    now = time.time()

    if identifier not in REQUEST_LOG:
        REQUEST_LOG[identifier] = []

    REQUEST_LOG[identifier] = [
        t for t in REQUEST_LOG[identifier]
        if now - t < RATE_LIMIT_WINDOW
    ]

    if len(REQUEST_LOG[identifier]) >= MAX_REQUESTS:
        return True

    REQUEST_LOG[identifier].append(now)

    return False
