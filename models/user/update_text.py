from db import create_connection


def update_text(user_id, new_text):
    with create_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT users_id FROM users WHERE users_id = ?", (user_id,))
        if cursor.fetchone() is None:
            return False

        cursor.execute("UPDATE users SET profile_text = ? WHERE users_id = ?", (new_text, user_id))
        conn.commit()
        return True
