from db import create_connection

import bcrypt


def create_user(password, email, name):
    with create_connection() as conn:
        cursor = conn.cursor()
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt).decode()
        query = "INSERT INTO users (users_name, email, password_user) VALUES (?, ?, ?)"
        cursor.execute(query, (name, email, hashed_password))
        conn.commit()
