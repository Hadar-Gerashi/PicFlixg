from db import create_connection
import os


def update_user_profile_image(user_id, filename):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT profile_image FROM users WHERE users_id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            old_filename = row[0]
            if old_filename:
                old_path = os.path.join("static/profile_images", old_filename)
                if os.path.exists(old_path):
                    os.remove(old_path)
        cursor.execute(
            "UPDATE users SET profile_image = ? WHERE users_id = ?",
            (filename, user_id)
        )
        conn.commit()
