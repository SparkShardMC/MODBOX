from backend.database.connection import get_connection

def create_user(username, email, password_hash):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, email, password_hash, verified, parent_approved) VALUES (?, ?, ?, ?, ?)",
        (username, email, password_hash, False, False)
    )

    conn.commit()

    return {"id": cursor.lastrowid}

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()

    if user:
        return dict(user)

    return None

def verify_user(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET verified=1 WHERE email=?",
        (email,)
    )

    conn.commit()

def approve_parent(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET parent_approved=1 WHERE email=?",
        (email,)
    )

    conn.commit()
