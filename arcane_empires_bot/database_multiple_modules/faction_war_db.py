def init_faction_war_table(conn):
    """
    Initializes the faction war outcomes table.
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faction_war (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            faction_one TEXT,
            faction_two TEXT,
            outcome TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)