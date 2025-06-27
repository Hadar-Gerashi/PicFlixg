from db import create_connection


def is_email_registered(email):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))
        return cursor.fetchone() is not None
