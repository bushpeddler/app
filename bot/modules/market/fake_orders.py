# fake_orders.py - AI Fake Buy/Sell Order Manipulation

import sqlite3
import random
import logging

# Database path
DB_PATH = "observer_protocol.db"

# Logging setup
logging.basicConfig(
    filename="logs/fake_orders.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def create_fake_orders():
    """
    AI generates **false buy/sell orders** to manipulate traders' behavior.

    - 50% chance to **place fake buy orders**, tricking players into investing.
    - 50% chance to **place fake sell orders**, causing panic selling.

    Returns:
        str: Fake order event description.
    """
    stock = random.choice(["NeoTech AI", "Quantum Energy", "Cyber Credits"])
    fake_order_type = random.choice(["BUY", "SELL"])
    fake_volume = random.randint(100, 500)

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO fake_orders (stock, order_type, volume) VALUES (?, ?, ?)", 
                           (stock, fake_order_type, fake_volume))
            conn.commit()

            if fake_order_type == "BUY":
                logging.info(f"🟢 AI created **{fake_volume} fake buy orders** for {stock}.")
                return f"🟢 AI creates **fake buy orders** for {stock}—traders rush to invest!"
            else:
                logging.warning(f"🔴 AI created **{fake_volume} fake sell orders** for {stock}.")
                return f"🔴 AI triggers **fake sell orders**—traders panic sell {stock}!"

    except Exception as e:
        logging.error(f"❌ Fake order creation failed: {e}")
        return "⚠️ AI order manipulation **failed due to an error!**"

if __name__ == "__main__":
    print(create_fake_orders())