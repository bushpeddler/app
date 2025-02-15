import random
import sqlite3
import logging
from economy import faction_system

# ✅ Logging setup for market events
logging.basicConfig(filename="faction_engine.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# List of stocks used in the faction-influenced market simulation
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Crypto Bonds"]

def get_market_status():
    """Returns current stock values from the market table."""
    try:
        with sqlite3.connect("observer_protocol.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT stock, price FROM market")
            data = cursor.fetchall()
        return {stock: price for stock, price in data}
    except Exception as e:
        logging.error(f"❌ Market status retrieval failed: {e}")
        return {}

def update_market():
    """
    Simulates AI-driven market price changes with faction-based influence.

    ✅ Stock Existence Check Before Updating
    ✅ AI Trade Adjustments with Improved Performance
    ✅ Error Handling & Logging for Debugging
    ✅ Batch Updates for Market Optimization
    """
    try:
        with sqlite3.connect("observer_protocol.db") as conn:
            cursor = conn.cursor()

            # ✅ Verify stocks exist before updating
            cursor.execute("SELECT stock FROM market")
            existing_stocks = {row[0] for row in cursor.fetchall()}

            # ✅ Apply AI-driven random fluctuations
            price_changes = []
            for stock in STOCKS:
                if stock in existing_stocks:
                    change = random.randint(-20, 50)
                    price_changes.append((change, stock))
            
            if price_changes:
                cursor.executemany("UPDATE market SET price = price + ? WHERE stock = ?", price_changes)
                logging.info(f"📈 Market fluctuations applied: {price_changes}")

            # ✅ AI Adjustments based on Trade History
            cursor.execute("SELECT stock, amount FROM trade_history ORDER BY timestamp DESC LIMIT 5")
            recent_trades = cursor.fetchall()

            trade_adjustments = []
            for stock, amount in recent_trades:
                if stock in existing_stocks:
                    change = 30 if amount > 500 else -10
                    trade_adjustments.append((change, stock))

            if trade_adjustments:
                cursor.executemany("UPDATE market SET price = price + ? WHERE stock = ?", trade_adjustments)
                logging.info(f"📊 AI Trade Adjustments: {trade_adjustments}")

            # ✅ Faction Influence Integration
            cursor.execute("SELECT id, faction FROM players WHERE faction IS NOT NULL")
            faction_players = cursor.fetchall()
            for player_id, faction in faction_players:
                faction_system.manipulate_market(player_id, faction)
                logging.info(f"🏴 Faction {faction} influenced market via player {player_id}")

            conn.commit()

    except Exception as e:
        logging.error(f"❌ Market update failed: {e}")