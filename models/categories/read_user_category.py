from db import create_connection


def read_user_categories(user_id):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.category_id
            FROM categories c
            JOIN user_categories uc ON c.category_id = uc.category_id
            WHERE uc.users_id = ?
        """, (user_id,))
        rows = cursor.fetchall()
        return [row.category_id for row in rows]
