from backend.database.parent_table import create_parent_request, get_parent_request, approve_parent_request
from backend.utils.date_utils import add_minutes_to_now
from backend.email.email_sender import send_email
import secrets

def generate_random_code(length=6):
    return secrets.token_hex(length // 2).upper()

def request_parent_approval(child_email, parent_email=None):
    code = generate_random_code()
    expires_at = add_minutes_to_now(60)

    request_id = create_parent_request(
        child_email=child_email,
        code=code,
        expires_at=expires_at,
        parent_email=parent_email
    )

    if parent_email:
        send_email(
            to_email=parent_email,
            template="parent_permission_email.html",
            data={"child_email": child_email, "code": code},
            subject="Parental Approval Required"
        )

    return request_id, code

def get_pending_request(child_email, code):
    return get_parent_request(child_email, code)
