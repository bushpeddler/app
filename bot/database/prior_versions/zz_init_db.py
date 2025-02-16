import sqlite3
import logging
import os
from database.players_db import init_players_table
from database.market_db import init_market_table
from database.trade_history_db import init_trade_history_table
from database.global_state_db import init_global_state_table
from database.faction_war_db import init_faction_war_table

# Logging Configuration
logging.basicConfig(
    filename="logs/database_init.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_PATH = "bot/database/observer_protocol.db"

def init_db():
    """
    Initializes all database tables and ensures the database file exists.
    """
    try:
        # Ensure the database directory exists
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

        # Connect to SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Initialize tables
        logging.info("🔹 Initializing database tables...")
        init_players_table(conn)
        logging.info("✅ Players table initialized.")
        
        init_market_table(conn)
        logging.info("✅ Market table initialized.")
        
        init_trade_history_table(conn)
        logging.info("✅ Trade history table initialized.")
        
        init_global_state_table(conn)
        logging.info("✅ Global state table initialized.")
        
        init_faction_war_table(conn)
        logging.info("✅ Faction war table initialized.")

        # Commit and close connection
        conn.commit()
        conn.close()

        logging.info("🎉 Database initialization complete!")

    except sqlite3.Error as e:
        logging.error(f"❌ Database initialization failed: {e}")

if __name__ == "__main__":
    init_db()