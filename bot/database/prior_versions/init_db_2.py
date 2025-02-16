"""
init_db.py - Database Initialization

Ensures the database (`observer_protocol.db`) is correctly structured.
If the database file doesn't exist, this script creates it with all necessary tables.
"""

import sqlite3
import os
from bot.database.faction_war_db import init_faction_war_table
from bot.database.global_state_db import init_global_state_table
from bot.database.market_db import init_market_table
from bot.database.trade_hx_db import init_trade_history_table
from bot.database.users_db import init_players_table

# Ensure the database file exists in the correct directory
DB_PATH = os.path.join(os.path.dirname(__file__), "observer_protocol.db")

def ensure_db_exists():
    """Creates an empty database file if it doesn't exist."""
    if not os.path.exists(DB_PATH):
        open(DB_PATH, "w").close()
        print(f"✅ Database file created: {DB_PATH}")

def init_db():
    """
    Initializes all database tables within observer_protocol.db.
    """
    ensure_db_exists()
    conn = sqlite3.connect(DB_PATH)

    init_players_table(conn)
    init_market_table(conn)
    init_trade_history_table(conn)
    init_global_state_table(conn)
    init_faction_war_table(conn)

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully.")

# This ensures the script runs correctly when opened in Textastic
if __name__ == "__main__":
    print("⚡ Preparing to initialize the database...")
    init_db()