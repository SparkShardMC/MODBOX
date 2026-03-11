from backend.database.user_table import create_user, get_user_by_email
from backend.security.password_hashing import hash_password, verify_password

def signup_user(username, email, password):
    existing = get_user_by_email(email)
    if existing:
        raise ValueError("Email already registered")
    hashed = hash_password(password)
    user = create_user(username=username, email=email, password_hash=hashed)
    return user

def login_user(email, password):
    user = get_user_by_email(email)
    if not user:
        return False
    return verify_password(user["password_hash"], password)
