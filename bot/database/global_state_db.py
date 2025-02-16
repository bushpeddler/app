import sqlite3

def init_global_state_table(conn):
    """
    Initializes the global economy state table.

    Fields:
    - `id` (Primary Key): Ensures only one state record exists.
    - `ai_status`: Current state of the Observer AI (e.g., Active, Dormant, Rogue).
    - `market_trend`: Tracks economic movement (Bull Market, Bear Market, Volatile).
    - `economic_stability`: Represents global stability on a scale of 1-100.
    - `faction_dominance`: Tracks the leading faction influencing the economy.
    - `last_updated`: Timestamp for the latest state change.

    Args:
        conn (sqlite3.Connection): Active SQLite database connection.
    """
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS global_state (
            id INTEGER PRIMARY KEY CHECK (id = 1),  -- Ensures a single row exists
            ai_status TEXT DEFAULT 'Active' CHECK(ai_status IN ('Active', 'Dormant', 'Rogue', 'Destroyed')),
            market_trend TEXT DEFAULT 'Stable' CHECK(market_trend IN ('Bull Market', 'Bear Market', 'Volatile', 'Stable')),
            economic_stability INTEGER DEFAULT 50 CHECK(economic_stability BETWEEN 0 AND 100),
            faction_dominance TEXT DEFAULT 'None',
            last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Ensure only one row exists in global_state
    cursor.execute("""
        INSERT OR IGNORE INTO global_state (id) VALUES (1)
    """)

    conn.commit()