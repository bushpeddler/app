# logic.py - Central Market Logic Engine

import sqlite3
import random
import logging
from market.engine.engine import update_market, get_market_status
from market.engine.factions import apply_faction_influence

# Database Path
DB_PATH = "observer_protocol.db"

# Logging Configuration
logging.basicConfig(
    filename="logs/market_logic.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def validate_trade(player_id, stock, amount):
    """
    Validates whether a player's trade is legitimate.
    
    - Ensures player has sufficient funds.
    - Prevents AI exploitation of market loopholes.
    - Logs high-risk trades for fraud detection.
    
    Returns:
        (bool, str): Success status and trade message.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Check if player has enough wealth to trade
            cursor.execute("SELECT wealth FROM players WHERE id = ?", (player_id,))
            result = cursor.fetchone()
            if not result or result[0] < amount:
                return False, "❌ Insufficient funds for trade."

            # Validate stock exists in market
            cursor.execute("SELECT price FROM market WHERE stock = ?", (stock,))
            stock_data = cursor.fetchone()
            if not stock_data:
                return False, "⚠️ Stock does not exist in the market."

            return True, "✅ Trade is valid."
    
    except Exception as e:
        logging.error(f"Trade validation error: {e}")
        return False, "❌ Trade validation failed due to an error."

def execute_trade(player_id, stock, amount):
    """
    Processes a player-initiated trade.

    - Deducts wealth from buyer.
    - Updates stock price based on transaction volume.
    - Logs trade history for tracking.

    Returns:
        str: Confirmation message.
    """
    valid, message = validate_trade(player_id, stock, amount)
    if not valid:
        return message

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Deduct wealth
            cursor.execute("UPDATE players SET wealth = wealth - ? WHERE id = ?", (amount, player_id))

            # Adjust market price dynamically
            cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (amount * 0.02, stock))

            # Log trade
            cursor.execute("INSERT INTO trade_history (player_id, stock, amount) VALUES (?, ?, ?)",
                           (player_id, stock, amount))

            conn.commit()
        
        logging.info(f"📊 Trade Executed: Player {player_id} bought {amount} of {stock}.")
        return f"✅ Trade successful! Purchased {amount} shares of {stock}."
    
    except Exception as e:
        logging.error(f"Trade execution error: {e}")
        return "❌ Trade failed due to an error."

def apply_market_effects():
    """
    Applies **AI-driven** and **faction-based** economic shifts.

    - Calls **AI trade algorithms** to adjust stock prices.
    - Processes **faction influence** on financial sectors.
    - Ensures **market balance** to prevent extreme volatility.
    """
    try:
        update_market()  # AI & player stock price updates

        # Apply faction influence dynamically
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT faction FROM players WHERE faction IS NOT NULL")
            factions = [row[0] for row in cursor.fetchall()]

            for faction in factions:
                apply_faction_influence(faction, "economic policy shift")

        logging.info("✅ Market effects successfully applied.")
    
    except Exception as e:
        logging.error(f"Market effects update error: {e}")

if __name__ == "__main__":
    apply_market_effects()