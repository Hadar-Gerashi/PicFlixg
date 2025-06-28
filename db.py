import pyodbc


def create_connection():
    conn_str = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=DESKTOP-F6TEN9G;DATABASE=social_network"
    try:
        connection = pyodbc.connect(conn_str)
        return connection
    except pyodbc.Error as e:
        print("Error connecting to the database:", e)
        return None
