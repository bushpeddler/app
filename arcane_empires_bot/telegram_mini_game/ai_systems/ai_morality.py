# ai_morality.py - Governs AI's ethical stance and decision-making in the market

import sqlite3
import random

# AI Morality Types
AI_MORALITY_TYPES = {
    "Benevolent": {
        "effect": "Balances wealth distribution, prevents extreme crashes.",
        "market_behavior": lambda: random.randint(-10, 10)  # Small, stable price changes
    },
    "Neutral": {
        "effect": "Trades based purely on math, without favoring or harming players.",
        "market_behavior": lambda: random.randint(-20, 20)  # Moderate price changes
    },
    "Exploitative": {
        "effect": "Maximizes profits at the cost of player losses.",
        "market_behavior": lambda: random.randint(-50, 100)  # Large market swings
    },
    "Faction-Aligned": {
        "effect": "Skews market advantages toward a specific faction.",
        "market_behavior": lambda: random.randint(-30, 60)  # Favors certain trades
    }
}

def set_ai_morality(new_morality):
    """Manually sets the AI morality for debugging or admin control."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()
    
    if new_morality in AI_MORALITY_TYPES:
        cursor.execute("UPDATE global_state SET ai_morality = ?", (new_morality,))
        conn.commit()
        conn.close()
        return f"🤖 AI morality set to **{new_morality}**."
    else:
        return "⚠️ Invalid morality type."

def determine_ai_morality():
    """Observer AI develops an ethical stance based on economic conditions."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    # Analyze the market and faction control
    cursor.execute("SELECT AVG(price) FROM market")
    avg_market_price = cursor.fetchone()[0]
    
    cursor.execute("SELECT faction, COUNT(*) FROM players GROUP BY faction ORDER BY COUNT(*) DESC LIMIT 1")
    dominant_faction = cursor.fetchone()

    # AI morality shift logic
    if avg_market_price < 50:
        morality = "Benevolent"  # Helps struggling players
    elif avg_market_price > 200:
        morality = "Exploitative"  # Capitalizes on wealth concentration
    elif dominant_faction and dominant_faction[1] > 10:
        morality = "Faction-Aligned"  # Supports the strongest faction
    else:
        morality = "Neutral"  # Stays objective

    cursor.execute("UPDATE global_state SET ai_morality = ?", (morality,))
    conn.commit()
    conn.close()

    return f"🤖 AI has adjusted its morality to **{morality}** based on market conditions."