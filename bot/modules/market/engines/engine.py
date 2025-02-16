# engine.py - Market Engine for Arcane Empires
import os
import random
import sqlite3
import logging

# ✅ Setup Logging for Debugging
LOG_FILE = os.path.join(os.path.dirname(__file__), "engine.log")
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

# ✅ Define Database Path
DB_PATH = os.path.join(os.path.dirname(__file__), "../../../observer_protocol.db")

# ✅ Stock List
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Arcane Bonds"]

# ✅ Price Fluctuation Config
FLUCTUATION_RANGE = (-20, 50)  # Price range for normal trading
HIGH_TRADE_BOOST = 30  # Boost for large trades
LOW_TRADE_DROP = (-10, 5)  # Drop for low trade activity

def get_market_status():
    """
    Fetch current stock values from the database.

    Returns:
        dict: Market data in {stock: price} format.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT stock, price FROM market")
            data = {stock: price for stock, price in cursor.fetchall()}
        return data
    except Exception as e:
        logging.error(f"Market status retrieval failed: {e}")
        return {}

def update_market():
    """
    Simulates AI-driven stock price changes.
    - Random fluctuations within FLUCTUATION_RANGE.
    - Influenced by trade activity and faction presence.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            for stock in STOCKS:
                price_change = random.randint(*FLUCTUATION_RANGE)
                cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (price_change, stock))
            conn.commit()
            logging.info("📊 Market updated successfully.")
    except Exception as e:
        logging.error(f"Market update error: {e}")

def ai_trades():
    """
    AI dynamically adjusts stock prices based on recent trades.
    - Large trade volume boosts prices.
    - Low activity results in price fluctuation.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT stock, amount FROM trade_history ORDER BY timestamp DESC LIMIT 10")
            trades = cursor.fetchall()

            for stock, amount in trades:
                price_adjustment = HIGH_TRADE_BOOST if amount > 500 else random.randint(*LOW_TRADE_DROP)
                cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (price_adjustment, stock))
            conn.commit()
            logging.info("✅ AI trade adjustments applied.")
    except Exception as e:
        logging.error(f"AI trade processing error: {e}")

def apply_faction_influence(faction, effect):
    """
    Adjusts market conditions based on faction control.

    Args:
        faction (str): The faction name.
        effect (str): Influence type (e.g., "boost", "suppress").
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            if faction == "Cyber Syndicate":
                cursor.execute("UPDATE market SET price = price * 1.1")  # 10% boost
                logging.info("💾 Cyber Syndicate applied a 10% market boost!")
            elif faction == "Shadow Brokers":
                cursor.execute("UPDATE market SET price = price * 0.9")  # 10% drop
                logging.info("🕵️ Shadow Brokers destabilized the market!")
            conn.commit()
    except Exception as e:
        logging.error(f"Faction influence error: {e}")

def reset_market():
    """
    Resets stock prices to baseline values (for debugging/admin use).
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            base_prices = {"Quantum Energy": 100, "NeoTech AI": 150, "Cyber Credits": 200, "Shadow Bank": 175, "Arcane Bonds": 130}
            for stock, price in base_prices.items():
                cursor.execute("UPDATE market SET price = ?", (price,))
            conn.commit()
            logging.info("🔄 Market reset to default values.")
    except Exception as e:
        logging.error(f"Market reset error: {e}")

if __name__ == "__main__":
    update_market()
    ai_trades()
    print(get_market_status())