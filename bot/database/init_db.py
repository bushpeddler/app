"""
init_db.py - Database Initialization Script

✅ Initializes all required database tables for Observer Protocol.
✅ Ensures database tables are created only if they don't already exist.
✅ Logs database setup for debugging.
"""

import sqlite3
import logging
from database.users_db import init_players_table
from database.market_db import init_market_table
from database.trade_hx_db import init_trade_history_table
from database.global_state_db import init_global_state_table
from database.faction_war_db import init_faction_war_table

# Configure logging
logging.basicConfig(
    filename="logs/database_setup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

DB_PATH = "observer_protocol.db"

def init_db():
    """
    Initializes all database tables required for game mechanics.
    Prevents duplicate table creation and logs status.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            
            # Initialize tables in sequence
            init_players_table(conn)
            init_market_table(conn)
            init_trade_history_table(conn)
            init_global_state_table(conn)
            init_faction_war_table(conn)

            conn.commit()  # ✅ Ensures all tables are saved

        logging.info("✅ Database initialization completed successfully.")
        print("✅ Database initialized successfully.")

    except sqlite3.Error as e:
        logging.error(f"❌ Database Initialization Failed: {e}")
        print(f"❌ Database Initialization Error: {e}")

if __name__ == "__main__":
    init_db()