"""
init_db.py - Database Initialization Script

✅ Ensures all required tables exist in observer_protocol.db.
✅ Logs setup process and prevents duplicate initialization.
✅ Handles missing database files.
"""

import sqlite3
import os
import logging
from database.players_db import init_players_table
from database.market_db import init_market_table
from database.trade_hx_db import init_trade_history_table
from database.global_state_db import init_global_state_table
from database.faction_war_db import init_faction_war_table

# Configure logging
LOG_PATH = "logs/database_setup.log"
DB_PATH = "observer_protocol.db"

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def ensure_db_exists():
    """Creates an empty database file if it doesn't exist."""
    if not os.path.exists(DB_PATH):
        open(DB_PATH, "w").close()
        print(f"✅ Created missing database file: {DB_PATH}")
        logging.info("Database file was missing and has been created.")

def init_db():
    """
    Initializes all necessary database tables.
    """
    ensure_db_exists()  # Ensures the DB file exists

    try:
        with sqlite3.connect(DB_PATH) as conn:
            init_players_table(conn)
            init_market_table(conn)
            init_trade_history_table(conn)
            init_global_state_table(conn)
            init_faction_war_table(conn)

        print("✅ Database initialization successful.")
        logging.info("Database initialized successfully.")

    except sqlite3.Error as e:
        print(f"❌ Database Initialization Failed: {e}")
        logging.error(f"Database Initialization Failed: {e}")

if __name__ == "__main__":
    print("⚡ Initializing database...")
    init_db()