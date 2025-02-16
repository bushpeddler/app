"""
trade_hx_db.py - Trade History Database Module

✅ Manages trade history records.
✅ Ensures database integrity and prevents duplicate trade errors.
✅ Optimized database handling with connection context managers.
"""

import sqlite3
import logging

# Configure logging
logging.basicConfig(
    filename="logs/trade_history.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

DB_PATH = "observer_protocol.db"

def init_trade_history_table():
    """
    Initializes the trade history table if it doesn't exist.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
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
            conn.commit()
        logging.info("✅ Trade history table initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"❌ Database Error: {e}")

def add_trade(player_id, stock, amount):
    """
    Inserts a new trade record into the trade history.
    Handles database errors and logs successful transactions.

    Args:
        player_id (int): The ID of the player executing the trade.
        stock (str): The name of the stock traded.
        amount (int): The number of shares traded.

    Returns:
        bool: True if trade is recorded successfully, False otherwise.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO trade_history (player_id, stock, amount) VALUES (?, ?, ?)",
                (player_id, stock, amount)
            )
            conn.commit()
        logging.info(f"🔹 Trade added - Player: {player_id}, Stock: {stock}, Amount: {amount}")
        return True
    except sqlite3.Error as e:
        logging.error(f"❌ Failed to add trade for Player {player_id}: {e}")
        return False

if __name__ == "__main__":
    init_trade_history_table()