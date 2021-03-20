from src.psql_connection import connection, close_connection
from src.queries import Queries as query

def select(params):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query.cielo, (params,))
    result = cursor.fetchall()
    close_connection(conn)
    return result
