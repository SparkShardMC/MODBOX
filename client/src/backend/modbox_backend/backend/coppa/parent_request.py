from backend.email.email_sender import send_email
from backend.database.parent_table import create_parent_request
from backend.verification.code_generator import generate_code
from backend.verification.expiration import generate_expiration_time

def request_parent_permission(child_email, username):
    code = generate_code()
    expiration = generate_expiration_time()

    parent_request = create_parent_request(
        child_email=child_email,
        username=username,
        code=code,
        expiration=expiration
    )

    return {
        "coppa_required": True,
        "parent_request_created": True,
        "request_id": parent_request["id"]
    }

def send_parent_email(parent_email, child_email, code):
    send_email(
        to_email=parent_email,
        template="parent_permission_email.html",
        data={
            "child_email": child_email,
            "code": code
        }
    )
