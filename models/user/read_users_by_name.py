from flask import jsonify
from db import create_connection


def read_users_by_name(query):
    with create_connection() as conn:
        cursor = conn.cursor()
        sql = "SELECT users_id, users_name FROM users WHERE users_name LIKE ?"
        cursor.execute(sql, (f'{query}%',))
        results = cursor.fetchall()
        users = [{"id": row[0], "name": row[1]} for row in results]
    return jsonify({"users": users})
