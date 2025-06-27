from db import create_connection


def create_category_video(video_id, category_id):
    with create_connection() as conn:
        cursor = conn.cursor()
        query = "INSERT INTO category_video(video_id, category_id) VALUES (?, ?)"
        cursor.execute(query, (video_id, category_id))
        cursor.commit()
