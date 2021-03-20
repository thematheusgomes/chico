import os
import psycopg2 as db
from src.log import Logger

LOG = Logger()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

def connection():
    try:
        conn = db.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        LOG.info('Connection established')
        return conn
    except Exception as e:
        LOG.error(f'Connection failed: {e}')

def close_connection(conn):
    conn.close()
    LOG.info('Connection closed')

if __name__ == '__main__':
    connection()
