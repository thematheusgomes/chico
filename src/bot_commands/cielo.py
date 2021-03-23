import numpy as np
import pandas as pd
from src.psql_connection.queries import Queries as query

def cielo_handler(db, args):
    sql_params = tuple(args.split(' '))
    conn = db.connection()
    df_transactions = pd.read_sql_query(query.cielo_transactions.format(sql_params), conn)
    users_list = df_transactions['user_id'].tolist()
    df_users = pd.read_sql_query(query.users.format(tuple(users_list)), conn)
    print(df_users)
