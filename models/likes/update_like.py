from db import create_connection


def update_like(user_id, video_id):
    with create_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
                SELECT 1 FROM likes WHERE users_id = ? AND video_id = ?
            """, (user_id, video_id))
        already_liked = cursor.fetchone()

        if already_liked:
            cursor.execute("""
                    DELETE FROM likes WHERE users_id = ? AND video_id = ?
                """, (user_id, video_id))
            action = "unliked"
        else:
            cursor.execute("""
                    INSERT INTO likes (users_id, video_id) VALUES (?, ?)
                """, (user_id, video_id))
            action = "liked"

        cursor.execute("""
                SELECT COUNT(*) FROM likes WHERE video_id = ?
            """, (video_id,))
        new_count = cursor.fetchone()[0]

        conn.commit()

    return {"status": "success", "action": action, "likes_count": new_count}
