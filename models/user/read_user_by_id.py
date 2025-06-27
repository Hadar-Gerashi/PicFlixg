from db import create_connection


def read_user_by_id(user_id):
    with create_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE users_id=?"
        cursor.execute(query, user_id)
        data = cursor.fetchone()
        print(data)
        return data
