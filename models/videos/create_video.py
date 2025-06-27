from db import create_connection


def create_video(user_id, video_url):
    with create_connection() as conn:
        cursor = conn.cursor()
        query = "INSERT INTO videos(users_id, video_url) VALUES (?, ?)"
        cursor.execute(query, (user_id, video_url))
