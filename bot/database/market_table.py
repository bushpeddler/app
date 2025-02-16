import sqlite3
import logging

# Logging Configuration
logging.basicConfig(
    filename="logs/market_init.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DEFAULT_STOCKS = {
    "Quantum Energy": 120,
    "NeoTech AI": 150,
    "Cyber Credits": 200,
    "Shadow Bank": 180,
    "Arcane Bonds": 90
}

def init_market_table(conn):
    """
    Initializes the market stocks table with default stock listings.
    """
    try:
        cursor = conn.cursor()

        # Create market table if it does not exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS market (
                stock TEXT PRIMARY KEY,
                price INTEGER DEFAULT 100
            )
        """)

        # Check if the table is empty
        cursor.execute("SELECT COUNT(*) FROM market")
        stock_count = cursor.fetchone()[0]

        # Insert default stocks only if the table is empty
        if stock_count == 0:
            for stock, price in DEFAULT_STOCKS.items():
                cursor.execute("INSERT INTO market (stock, price) VALUES (?, ?)", (stock, price))
            logging.info(f"✅ Market table initialized with default stocks: {list(DEFAULT_STOCKS.keys())}")

        conn.commit()

    except sqlite3.Error as e:
        logging.error(f"❌ Market table initialization failed: {e}")