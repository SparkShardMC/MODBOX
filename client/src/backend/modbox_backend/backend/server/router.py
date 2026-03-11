from flask import Flask, request, jsonify
from backend.auth.signup import signup_user, login_user
from backend.verification.verification_codes import verify_code
from backend.coppa.parent_request import request_parent_approval, approve_parent_account
from backend.sessions.session_manager import create_session, get_session
from backend.security.username_blacklist import is_username_allowed
from backend.security.rate_limits import is_rate_limited
from backend.database.user_table import get_user_by_email
from backend.email.email_sender import send_email
from backend.utils.validators import is_valid_email, is_valid_username, is_strong_password
from backend.utils.date_utils import add_minutes_to_now

app = Flask(__name__)

@app.route("/auth/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if is_rate_limited(email):
        return jsonify({"error": "Too many requests"}), 429

    if not is_valid_email(email):
        return jsonify({"error": "Invalid email"}), 400

    if not is_valid_username(username):
        return jsonify({"error": "Invalid username"}), 400

    if not is_strong_password(password):
        return jsonify({"error": "Weak password"}), 400

    if not is_username_allowed(username):
        return jsonify({"error": "Username not allowed"}), 400

    user = signup_user(username, email, password)

    code = verify_code.generate_verification_code()
    expiration = add_minutes_to_now(10)
    verify_code.store_verification_code(email, code, expiration)

    send_email(
        to_email=email,
        template="verification_email.html",
        data={"code": code},
        subject="Verify Your MODBOX Account"
    )

    return jsonify({"message": "User created, verification email sent"}), 201

@app.route("/auth/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if is_rate_limited(email):
        return jsonify({"error": "Too many requests"}), 429

    user = get_user_by_email(email)
    if not user or not login_user(email, password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_session(user["id"])
    return jsonify({"token": token}), 200

@app.route("/verification/verify", methods=["POST"])
def verify():
    data = request.json
    email = data.get("email")
    code = data.get("code")

    if verify_code.validate_verification(email, code):
        return jsonify({"message": "Email verified"}), 200
    return jsonify({"error": "Invalid or expired code"}), 400

# ---------------------------
# COPPA Endpoints
# ---------------------------

@app.route("/coppa/request", methods=["POST"])
def coppa_request():
    data = request.json
    child_email = data.get("child_email")
    parent_email = data.get("parent_email")  # optional

    request_id, code = request_parent_approval(child_email, parent_email)

    return jsonify({"message": "Parent approval requested", "code": code}), 201

@app.route("/coppa/approve", methods=["POST"])
def coppa_approve():
    data = request.json
    child_email = data.get("child_email")
    code = data.get("code")

    if approve_parent_account(child_email, code):
        return jsonify({"message": "Child account approved"}), 200
    return jsonify({"error": "Invalid or expired code"}), 400

@app.route("/user/me", methods=["GET"])
def get_user():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "No token provided"}), 401
    session = get_session(token)
    if not session:
        return jsonify({"error": "Invalid session"}), 401
    user = get_user_by_email(session["user_id"])
    return jsonify({"user": user}), 200

if __name__ == "__main__":
    app.run(debug=True)
