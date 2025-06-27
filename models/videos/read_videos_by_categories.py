from db import create_connection


def read_videos_by_categories(category_ids):
    with create_connection() as conn:
        placeholders = ','.join(['%s'] * len(category_ids))
        query = f"""
        SELECT DISTINCT v.*
        FROM videos v
        JOIN video_categories vc ON v.id = vc.video_id
        WHERE vc.category_id IN ({placeholders})
     """
        cursor = conn.cursor()
        cursor.execute(query, category_ids)
        return cursor.fetchall()
