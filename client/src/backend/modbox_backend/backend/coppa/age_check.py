from datetime import date
from backend.coppa.parent_request import request_parent_permission

COPPA_AGE_LIMIT = 13

def calculate_age(birthdate):
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def check_user_age(birthdate, email, username):
    age = calculate_age(birthdate)

    if age < COPPA_AGE_LIMIT:
        return request_parent_permission(email, username)

    return {
        "coppa_required": False,
        "allowed": True
    }
