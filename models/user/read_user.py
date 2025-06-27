from db import create_connection


def read_user(password, name):
    with create_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE password_user = ? AND users_name = ?"
        cursor.execute(query, (password, name))
        data = cursor.fetchone()
        print(data)
        return data
