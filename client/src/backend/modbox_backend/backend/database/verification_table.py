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
    CREATE TABLE IF NOT EXISTS verification_codes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(100) NOT NULL,
        code VARCHAR(20) NOT NULL,
        expires_at TIMESTAMP NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def store_verification_code(email, code, expires_at):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO verification_codes (email, code, expires_at) VALUES (%s, %s, %s)",
        (email, code, expires_at)
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_verification_code(email, code):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM verification_codes WHERE email=%s AND code=%s",
        (email, code)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def delete_verification_code(email, code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM verification_codes WHERE email=%s AND code=%s",
        (email, code)
    )
    conn.commit()
    cursor.close()
    conn.close()
