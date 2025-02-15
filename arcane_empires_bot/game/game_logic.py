"""
game_logic.py - Core Gameplay Mechanics

This module implements:
- Trade: Stock trading with market volatility effects.
- Hack AI: Introduces penalties for failed hacks.
- Join Faction: Assigns players to factions with market influence.

This file connects with market_engine.py, faction_system.py, and observer_protocol.db.
"""

import sqlite3
import random
from economy import market_engine  # ✅ Fixed import
import faction_system

def trade(player_id, stock, amount):
    """
    Processes a trade while triggering market volatility.

    Args:
        player_id (int): The player's unique identifier.
        stock (str): Stock name or symbol to trade.
        amount (int): Number of shares to buy.

    Returns:
        str: Trade confirmation or failure message.
    """
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()

        # ✅ Ensure player exists and fetch their wealth
        cursor.execute("SELECT wealth, market_restricted_until FROM players WHERE id = ?", (player_id,))
        result = cursor.fetchone()

        if not result:
            return "❌ Player not found!"

        player_wealth, restriction = result

        if restriction:
            return "⛔ Market access restricted due to AI detection! Try again later."

        # ✅ Ensure stock exists before proceeding
        cursor.execute("SELECT price FROM market WHERE stock = ?", (stock,))
        stock_result = cursor.fetchone()

        if not stock_result:
            return f"❌ Stock '{stock}' not found!"
        
        stock_price = stock_result[0]
        total_cost = stock_price * amount

        if player_wealth < total_cost:
            return "❌ Insufficient funds!"

        new_wealth = player_wealth - total_cost

        # ✅ Transaction: Update player's wealth & record trade
        cursor.execute("UPDATE players SET wealth = ? WHERE id = ?", (new_wealth, player_id))
        cursor.execute("INSERT INTO trade_history (player_id, stock, amount) VALUES (?, ?, ?)", (player_id, stock, amount))
        conn.commit()

    # ✅ Call `market_engine.update_market()`
    market_engine.update_market(stock, amount)

    return f"✅ Trade successful! {amount} shares of {stock} bought at {stock_price} credits each."

def hack_ai(player_id):
    """
    Allows a player to hack the Observer AI.

    Success: Grants a market advantage.
    Failure: Market access is restricted for 10 minutes.

    Args:
        player_id (int): The player's unique identifier.

    Returns:
        str: Result message.
    """
    success = random.choice([True, False])

    if success:
        return "🕵️ AI hacked successfully! Temporary market advantage enabled."
    else:
        restrict_player_market_access(player_id, 10)
        return "⚠️ AI detected your attempt! Market access restricted for 10 minutes."

def restrict_player_market_access(player_id, duration=10):
    """
    Restricts a player's market access for a set duration.

    Args:
        player_id (int): The player's ID.
        duration (int): Restriction duration in minutes.
    """
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE players SET market_restricted_until = datetime('now', '+{} minutes') WHERE id = ?".format(duration), (player_id,))
        conn.commit()

def join_faction(player_id, faction):
    """
    Assigns a player to a faction.

    Args:
        player_id (int): Player's ID.
        faction (str): Chosen faction.

    Returns:
        str: Confirmation message.
    """
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE players SET faction = ? WHERE id = ?", (faction, player_id))
        conn.commit()
    return f"✅ You have joined **{faction}**!"