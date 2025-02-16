"""
lore.py - Tracks and Manages Economic History in Arcane Empires

✅ Records major market events (crashes, booms, financial conspiracies).
✅ Logs factional influence over economic history.
✅ Stores player-driven financial manipulations & legendary traders.
✅ Allows AI to learn from past financial cycles for adaptive trading.
"""

import sqlite3
import logging

# Database path
DB_PATH = "observer_protocol.db"

# Configure logging
logging.basicConfig(
    filename="logs/economic_lore.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def record_market_event(event_name, description, impact_level):
    """
    Logs significant economic events in the global financial archive.

    Args:
        event_name (str): The name of the event (e.g., "AI Market Takeover").
        description (str): Summary of the event’s impact.
        impact_level (str): "Minor", "Moderate", or "Major" based on disruption level.
    
    Returns:
        str: Confirmation of event storage.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO market_history (event_name, description, impact_level, timestamp)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            """, (event_name, description, impact_level))
            conn.commit()

        logging.info(f"📜 Market Event Logged: {event_name} - {impact_level} impact.")
        return f"✅ {event_name} recorded in financial archives."
    
    except Exception as e:
        logging.error(f"❌ Failed to log market event: {e}")
        return "⚠️ Error logging market event."

def track_legendary_trader(player_id, username, achievement):
    """
    Records a player's economic legacy for future game cycles.

    Args:
        player_id (int): Unique player identifier.
        username (str): Player’s in-game name.
        achievement (str): Notable financial impact (e.g., "First player to create an economic monopoly").
    
    Returns:
        str: Confirmation message.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO legendary_traders (player_id, username, achievement, timestamp)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            """, (player_id, username, achievement))
            conn.commit()

        logging.info(f"🏆 Legendary Trader Recorded: {username} - {achievement}.")
        return f"🏆 {username} is now part of economic history!"
    
    except Exception as e:
        logging.error(f"❌ Failed to log legendary trader: {e}")
        return "⚠️ Error recording legendary trader."

def retrieve_historical_trends():
    """
    Fetches past economic events to allow players and AI to analyze financial history.

    Returns:
        list: Recent market events and their impacts.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT event_name, description, impact_level, timestamp FROM market_history ORDER BY timestamp DESC LIMIT 5")
            events = cursor.fetchall()

        logging.info(f"📜 Retrieved latest market history trends.")
        return events if events else "📜 No historical market events found."
    
    except Exception as e:
        logging.error(f"❌ Failed to retrieve market history: {e}")
        return "⚠️ Error fetching historical data."

# Example Usage
if __name__ == "__main__":
    print(record_market_event("AI Trading Uprising", "Observer AI controlled the stock market, out-trading humans.", "Major"))
    print(track_legendary_trader(42, "ShadowTrader", "First to manipulate a faction-driven stock crash."))
    print(retrieve_historical_trends())