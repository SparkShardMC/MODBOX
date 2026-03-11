from backend.database.connection import get_connection

def create_verification(email, code, expiration):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO verifications (email, code, expiration) VALUES (?, ?, ?)",
        (email, code, expiration)
    )

    conn.commit()

    return {"id": cursor.lastrowid}

def get_verification(code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM verifications WHERE code=?",
        (code,)
    )

    result = cursor.fetchone()

    if result:
        return dict(result)

    return None

def delete_verification(code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM verifications WHERE code=?",
        (code,)
    )

    conn.commit()
