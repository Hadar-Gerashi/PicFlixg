from db import create_connection


def read_user_by_email(email):
    with create_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE email = ?"
        cursor.execute(query, (email,))
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'users_name': row[1],
                'email': row[2],
                'password_user': row[3]
            }
        return None
