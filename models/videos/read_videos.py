from db import create_connection


def read_videos(user_id):
    with create_connection() as conn:
        cursor = conn.cursor()
        query = """
           SELECT 
               sub.video_id, 
                    sub.users_id,
                         u.users_name,
               sub.video_url, 
               u.profile_image,
               ISNULL(like_counts.like_count, 0) AS likes_count
           FROM (
               SELECT 
                   v.video_id, 
                   v.video_url, 
                   v.users_id,
                   CASE 
                       WHEN EXISTS (
                           SELECT 1 
                           FROM category_video cv2
                           JOIN user_categories uc2 ON cv2.category_id = uc2.category_id
                           WHERE cv2.video_id = v.video_id AND uc2.users_id = ?
                       ) THEN 0
                       ELSE 1
                   END AS preference_order,
                   NEWID() AS random_order
               FROM videos v
           ) AS sub
           JOIN users u ON sub.users_id = u.users_id
           LEFT JOIN (
               SELECT video_id, COUNT(*) AS like_count
               FROM likes
               GROUP BY video_id
           ) AS like_counts ON sub.video_id = like_counts.video_id
           GROUP BY 
               sub.video_id, sub.video_url, sub.users_id, u.users_name, u.profile_image, sub.preference_order, sub.random_order, like_counts.like_count
           ORDER BY 
               sub.preference_order, 
               sub.random_order
           """
        cursor.execute(query, (user_id,))
        data = cursor.fetchall()
        print(data)
        return data
