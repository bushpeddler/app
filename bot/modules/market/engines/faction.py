# factions.py - Faction Market Influence System
import os
import random
import sqlite3
import logging
from market.engine import get_market_status

# ✅ Setup Logging for Debugging
LOG_FILE = os.path.join(os.path.dirname(__file__), "factions.log")
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

# ✅ Define Database Path
DB_PATH = os.path.join(os.path.dirname(__file__), "../../../observer_protocol.db")

# ✅ Stock List (Aligned with Market Engine)
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Crypto Bonds"]

# ✅ Faction-Based Economic Effects
FACTION_EFFECTS = {
    "Cyber Syndicate": {"boost": 1.15, "target": "NeoTech AI"},
    "Shadow Brokers": {"drop": 0.85, "target": "Shadow Bank"},
    "Technocrats": {"stability": True},  # Prevents volatility
    "Free Traders": {"randomized": True},  # Adds randomness
}

def get_faction_influence():
    """
    Retrieves faction-related economic influences from the database.

    Returns:
        dict: Faction market impact settings.
    """
    influence_data = {}
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT faction, effect, target FROM faction_market_influence")
            for faction, effect, target in cursor.fetchall():
                influence_data[faction] = {"effect": effect, "target": target}
    except Exception as e:
        logging.error(f"❌ Failed to retrieve faction market influence: {e}")
    return influence_data

def apply_faction_effects():
    """
    Adjusts market conditions based on faction presence and control.
    - Influences targeted stock prices based on faction dominance.
    - Prevents economic stagnation by dynamically adjusting markets.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # ✅ Fetch Market Status & Faction Influence
            market_data = get_market_status()
            faction_influence = get_faction_influence()

            for faction, impact in FACTION_EFFECTS.items():
                if faction in faction_influence:
                    stock = faction_influence[faction]["target"]
                    effect = faction_influence[faction]["effect"]

                    if stock in market_data:
                        if "boost" in impact:
                            cursor.execute("UPDATE market SET price = price * ? WHERE stock = ?", (impact["boost"], stock))
                        elif "drop" in impact:
                            cursor.execute("UPDATE market SET price = price * ? WHERE stock = ?", (impact["drop"], stock))
                        elif "stability" in impact:
                            cursor.execute("UPDATE market SET price = (price + (SELECT AVG(price) FROM market) ) / 2 WHERE stock = ?", (stock,))
                        elif "randomized" in impact:
                            cursor.execute("UPDATE market SET price = price * ? WHERE stock = ?", (random.uniform(0.9, 1.1), stock))

                        logging.info(f"🏴 {faction} influenced {stock} - Effect applied.")

            conn.commit()

    except Exception as e:
        logging.error(f"❌ Faction market effect application failed: {e}")

def reset_faction_influence():
    """
    Resets faction-based influence in the economy.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM faction_market_influence")
            conn.commit()
            logging.info("🔄 Faction influence reset.")
    except Exception as e:
        logging.error(f"❌ Faction reset failed: {e}")

if __name__ == "__main__":
    apply_faction_effects()