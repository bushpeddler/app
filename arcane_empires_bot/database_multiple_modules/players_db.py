import sqlite3

def init_players_table(conn):
    """
    Initializes the players table.
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            username TEXT,
            wealth INTEGER DEFAULT 1000,
            faction TEXT DEFAULT 'Neutral'
        )
    """)