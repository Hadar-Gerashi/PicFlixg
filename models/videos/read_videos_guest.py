from db import create_connection


def read_videos_guest():
    with create_connection() as conn:
        cursor = conn.cursor()
        query = """
                   SELECT
                   v.video_id,
                       v.users_id,
                       u.users_name,
                       v.video_url,
                       u.profile_image,
                       COUNT(l.like_id) AS likes_count
                   FROM videos v
                   JOIN users u ON v.users_id = u.users_id
                   LEFT JOIN likes l ON v.video_id = l.video_id
                   GROUP BY v.video_id, v.users_id, u.users_name, v.video_url, v.created_at ,u.profile_image
                   ORDER BY v.created_at DESC
               """
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        return data
