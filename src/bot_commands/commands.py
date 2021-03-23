from src.bot_commands.cielo import cielo_handler
from src.psql_connection.database import Database

DB = Database()

def commands_handler(command, args):
    if command == '/cieloalert':
        cielo_handler(DB, args)
