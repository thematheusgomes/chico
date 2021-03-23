import os
import psycopg2 as db
from src.log import Logger

LOG = Logger()

db_params = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_DATABASE'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

class Database:
    def __init__(self):
        try:
            LOG.info('Connecting to the PostgreSQL database...')
            self.conn = db.connect(**db_params)
            self.cur = self.connection.cursor()
            LOG.info('Connected')
        except Exception as e:
            LOG.error(f'Connection failed: {e}')

    def connection(self):
        return self.conn

    def query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
