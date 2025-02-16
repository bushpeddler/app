# bubbles.py - AI-Driven Market Bubbles & Crashes

import sqlite3
import random
import logging

# Database path
DB_PATH = "observer_protocol.db"

# High-risk assets targeted by AI for speculative bubbles
BUBBLE_STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits"]

# Configure logging
logging.basicConfig(
    filename="logs/bubbles.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def generate_bubble():
    """
    AI artificially inflates an asset before a future crash.

    - **Doubles stock price** to create an illusion of growth.
    - **Logs the bubble formation** for tracking.
    
    Returns:
        str: Bubble event outcome.
    """
    stock = random.choice(BUBBLE_STOCKS)

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE market SET price = price * 2 WHERE stock = ?", (stock,))
            conn.commit()

        logging.info(f"🔥 Asset Bubble Created: {stock} price doubled.")
        return f"🔥 **Asset Bubble Detected!** {stock} price **doubled**, but may crash soon!"

    except Exception as e:
        logging.error(f"❌ Bubble creation failed: {e}")
        return "⚠️ AI bubble manipulation failed due to an error!"

def crash_bubble():
    """
    AI crashes a previously inflated stock, wiping out its value.

    - **Reduces stock value by 60%** to simulate a bubble burst.
    - **Logs market collapse event**.

    Returns:
        str: Market crash event outcome.
    """
    stock = random.choice(BUBBLE_STOCKS)

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE market SET price = price * 0.4 WHERE stock = ?", (stock,))
            conn.commit()

        logging.warning(f"💥 Market Crash Triggered: {stock} lost 60% of its value.")
        return f"💥 **Market Crash!** {stock} lost **60% of its value overnight!**"

    except Exception as e:
        logging.error(f"❌ Market crash failed: {e}")
        return "⚠️ AI market crash intervention failed!"

if __name__ == "__main__":
    print(generate_bubble())
    print(crash_bubble())