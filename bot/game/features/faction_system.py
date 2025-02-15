"""
faction_system.py - Manages faction-based financial influence

This module provides functions to retrieve faction effects and manipulate the market based on a player's faction.
Each faction has unique bonuses and trade effects.
"""

import sqlite3
import random

# Predefined faction data
FACTIONS = {
    "Syndicate": {
        "bonus": "illegal_trade",
        "effect": "Black market goods are 20% cheaper, but legal trades are taxed higher."
    },
    "Technocrats": {
        "bonus": "ai_optimization",
        "effect": "AI prevents market crashes, but trade restrictions limit profits."
    },
    "Decentralists": {
        "bonus": "crypto_volatility",
        "effect": "Crypto-based assets fluctuate wildly, offering high risk and high reward."
    }
}

def get_faction_effects(player_id):
    """
    Retrieves the trade effects for the player's faction.

    Args:
        player_id (int): The player's unique identifier.

    Returns:
        dict: A dictionary containing the 'bonus' and 'effect' for the player's faction.
              If the player is not affiliated with any faction, returns default values.
    """
    query = "SELECT faction FROM players WHERE id = ?"
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, (player_id,))
        result = cursor.fetchone()
    
    faction = result[0] if result else None
    return FACTIONS.get(faction, {"bonus": "None", "effect": "No faction benefits."})

def manipulate_market(player_id):
    """
    Allows a player to influence the market based on their faction's abilities.

    Args:
        player_id (int): The player's unique identifier.

    Returns:
        str: A message describing the outcome of the market manipulation attempt.
    """
    query = "SELECT faction FROM players WHERE id = ?"
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, (player_id,))
        result = cursor.fetchone()
        
        if not result:
            return "⚠️ Player not found."

        faction = result[0]
        
        if faction == "Syndicate":
            # Black market influence increases Shadow Bank stocks
            change = random.randint(10, 30)
            cursor.execute("UPDATE market SET price = price + ? WHERE stock = 'Shadow Bank'", (change,))
            result_msg = "💰 The Syndicate increased underground wealth! Shadow Bank stocks rise!"
        
        elif faction == "Technocrats":
            # AI optimization stabilizes the market
            cursor.execute("UPDATE market SET price = price * 0.9")
            result_msg = "🤖 AI optimization prevented a stock crash!"
        
        elif faction == "Decentralists":
            # Crypto volatility: random fluctuation for Crypto Bonds
            fluctuation = random.choice([-30, 50])
            cursor.execute("UPDATE market SET price = price + ? WHERE stock = 'Crypto Bonds'", (fluctuation,))
            result_msg = f"📈 Crypto market fluctuates wildly! New price swing: {fluctuation}%"
        
        else:
            result_msg = "⚠️ You need to join a faction before influencing the market."

        conn.commit()
    
    return result_msg