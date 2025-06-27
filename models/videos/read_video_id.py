from db import create_connection


def read_video_id(users_id, video_url):
    with create_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT video_id FROM videos WHERE users_id = ? AND video_url = ?"
        cursor.execute(query, (users_id, video_url))
        data = cursor.fetchone()[0]
        print(data)
        return data
