from db import create_connection


def read_user_videos(user_id):
    with create_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT video_id, video_url FROM videos WHERE users_id = ?"
        cursor.execute(query, (user_id,))
        data = cursor.fetchall()
        print(data)
        return data
