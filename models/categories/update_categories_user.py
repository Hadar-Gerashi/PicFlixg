from db import create_connection


def update_categories_user(user_id, category_ids):
    with create_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM user_categories WHERE users_id = ?", (user_id,))

        for cat_id in category_ids:
            cursor.execute("INSERT INTO user_categories (users_id, category_id) VALUES (?, ?)", (user_id, cat_id))

        conn.commit()
