import mysql.connector
from mysql.connector import Error
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "user": "modbox_user",
    "password": "your_password",
    "database": "modbox_db"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS parent_requests (
        id INT AUTO_INCREMENT PRIMARY KEY,
        child_email VARCHAR(100) NOT NULL,
        parent_email VARCHAR(100),
        code VARCHAR(20) NOT NULL,
        approved BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def create_parent_request(child_email, code, expires_at, parent_email=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO parent_requests (child_email, parent_email, code, expires_at) VALUES (%s, %s, %s, %s)",
        (child_email, parent_email, code, expires_at)
    )
    conn.commit()
    request_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return request_id

def get_parent_request(child_email, code):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM parent_requests WHERE child_email=%s AND code=%s",
        (child_email, code)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def approve_parent_request(child_email, code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE parent_requests SET approved=TRUE WHERE child_email=%s AND code=%s",
        (child_email, code)
    )
    conn.commit()
    cursor.close()
    conn.close()
