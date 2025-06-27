from db import create_connection


def delete_video_by_id(video_id, table_name):
    allowed_tables = {"videos", "category_video"}
    if table_name not in allowed_tables:
        raise ValueError("Invalid table name")
    with create_connection() as conn:
        cursor = conn.cursor()
        query = f"DELETE FROM {table_name} WHERE video_id = ?"
        cursor.execute(query, (video_id,))
        conn.commit()
