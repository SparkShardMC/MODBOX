from backend.database.parent_table import get_parent_request, approve_child_account, deny_child_account
from backend.verification.expiration import is_code_expired

def approve_request(code):
    request = get_parent_request(code)

    if not request:
        return {"approved": False, "reason": "invalid_code"}

    if is_code_expired(request["expiration"]):
        return {"approved": False, "reason": "expired"}

    approve_child_account(request["child_email"])

    return {"approved": True}

def deny_request(code):
    request = get_parent_request(code)

    if not request:
        return {"denied": False, "reason": "invalid_code"}

    deny_child_account(request["child_email"])

    return {"denied": True}
