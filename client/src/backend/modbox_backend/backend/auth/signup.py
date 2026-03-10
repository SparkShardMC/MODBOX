from datetime import datetime
from ..server.config import COPPA_MIN_AGE
from .password_validation import validate_password
from .username_validation import validate_username

def calculate_age(dob):
    today = datetime.utcnow().date()
    birth = datetime.strptime(dob, "%Y-%m-%d").date()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age

def process_signup(username, email, password, dob):
    username_valid, username_error = validate_username(username)
    if not username_valid:
        return {"success": False, "error": username_error}

    password_valid, password_error = validate_password(password)
    if not password_valid:
        return {"success": False, "error": password_error}

    age = calculate_age(dob)

    if age < COPPA_MIN_AGE:
        return {
            "success": False,
            "coppa_required": True,
            "message": "Parental approval required"
        }

    return {
        "success": True,
        "coppa_required": False,
        "username": username,
        "email": email,
        "dob": dob
    }
