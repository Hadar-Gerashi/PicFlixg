from db import create_connection


def read_categories():
    with create_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM categories"
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        return data
