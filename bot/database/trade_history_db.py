import sqlite3

def init_trade_history_table(conn):
    """
    Initializes the trade history table.
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trade_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            stock TEXT,
            amount INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

def add_trade(player_id, stock, amount):
    """
    Inserts a new trade record into the trade history.
    """
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO trade_history (player_id, stock, amount) VALUES (?, ?, ?)",
        (player_id, stock, amount)
    )
    conn.commit()
    conn.close()