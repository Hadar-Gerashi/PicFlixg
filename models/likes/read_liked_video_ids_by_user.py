from db import create_connection


def read_liked_video_ids_by_user(user_id):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT video_id FROM likes WHERE users_id = ?", (user_id,))
        liked_videos = {row[0] for row in cursor.fetchall()}
    return liked_videos
