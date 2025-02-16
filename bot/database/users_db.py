import sqlite3

def init_players_table(conn):
    """
    Initializes the players table if it doesn't already exist.

    Structure:
    - `id` (Primary Key, Auto-Increment)
    - `username` (Unique Identifier)
    - `wealth` (Default: 1000 credits)
    - `faction` (Default: 'Neutral')
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                wealth INTEGER DEFAULT 1000,
                faction TEXT DEFAULT 'Neutral'
            )
        """)
        conn.commit()  # ✅ Saves table creation
        print("✅ Players table initialized.")
    except sqlite3.Error as e:
        print(f"❌ Database Error: {e}")