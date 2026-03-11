from backend.sessions.token_generator import generate_token

SESSIONS = {}

def create_session(user_id):
    token = generate_token()

    SESSIONS[token] = {
        "user_id": user_id
    }

    return token

def get_session(token):
    if token in SESSIONS:
        return SESSIONS[token]

    return None

def delete_session(token):
    if token in SESSIONS:
        del SESSIONS[token]
