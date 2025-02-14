import sqlite3

def init_db():
    """
    Initializes the database with required tables for players, market, trade history, AI state, and faction wars.
    """
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            username TEXT,
            wealth INTEGER DEFAULT 1000,
            faction TEXT DEFAULT 'Neutral',
            market_restricted_until DATETIME DEFAULT NULL  -- Handles AI hack restrictions
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS market (
            stock TEXT PRIMARY KEY,
            price INTEGER DEFAULT 100
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trade_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            stock TEXT,
            amount INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS global_state (
            ai_status TEXT DEFAULT 'Active',
            ai_morality TEXT DEFAULT 'Neutral'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faction_war (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            faction_one TEXT,
            faction_two TEXT,
            outcome TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Optimize query speed by adding indexes
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_trade_history_player ON trade_history (player_id)")
    
    conn.commit()
    conn.close()

def add_trade(player_id, stock, amount):
    """
    Stores trade history in the database.
    """
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO trade_history (player_id, stock, amount) VALUES (?, ?, ?)", (player_id, stock, amount))
        conn.commit()