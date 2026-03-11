from backend.database.parent_table import get_parent_request, approve_parent_request
from datetime import datetime

def approve_parent_account(child_email, code):
    request = get_parent_request(child_email, code)
    if not request:
        return False

    now = datetime.utcnow()
    if now > request["expires_at"]:
        return False

    approve_parent_request(child_email, code)
    return True
