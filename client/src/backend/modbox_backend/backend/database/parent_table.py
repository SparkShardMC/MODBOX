from backend.database.connection import get_connection

def create_parent_request(child_email, username, code, expiration):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO parent_requests (child_email, username, code, expiration, approved) VALUES (?, ?, ?, ?, ?)",
        (child_email, username, code, expiration, False)
    )

    conn.commit()

    return {"id": cursor.lastrowid}

def get_parent_request(code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM parent_requests WHERE code=?",
        (code,)
    )

    result = cursor.fetchone()

    if result:
        return dict(result)

    return None

def approve_child_account(child_email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE parent_requests SET approved=1 WHERE child_email=?",
        (child_email,)
    )

    conn.commit()

def deny_child_account(child_email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM parent_requests WHERE child_email=?",
        (child_email,)
    )

    conn.commit()
