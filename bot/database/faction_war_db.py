import sqlite3

def init_faction_war_table(conn):
    """
    Initializes the faction war outcomes table if it does not already exist.

    Fields:
    - `id` (Primary Key): Unique ID for each war record.
    - `faction_one` & `faction_two`: The competing factions.
    - `outcome`: The result of the war.
    - `winner`: The winning faction (for easier queries).
    - `duration`: Length of the war in in-game time (optional, for analytics).
    - `timestamp`: Auto-generated time of event.

    Args:
        conn (sqlite3.Connection): Active SQLite database connection.
    """
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faction_war (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            faction_one TEXT NOT NULL,
            faction_two TEXT NOT NULL,
            outcome TEXT NOT NULL CHECK(outcome IN ('Victory', 'Defeat', 'Stalemate')),
            winner TEXT DEFAULT NULL,  -- Stores the winning faction for faster lookups
            duration INTEGER DEFAULT 0, -- Duration of war (optional, can be updated later)
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()