import re

def is_valid_email(email):
    """
    Check if the email is in a valid format.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def is_valid_username(username, min_len=3, max_len=20):
    """
    Check username length and allowed characters.
    """
    if not (min_len <= len(username) <= max_len):
        return False
    pattern = r"^[A-Za-z0-9_]+$"
    return re.match(pattern, username) is not None

def is_strong_password(password):
    """
    Check if password meets basic strength requirements:
    - At least 8 characters
    - At least one lowercase, one uppercase, one digit
    """
    if len(password) < 8:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True
