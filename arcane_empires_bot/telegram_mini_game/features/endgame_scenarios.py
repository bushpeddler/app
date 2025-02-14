# endgame_scenarios.py - Defines game-ending economic events and victory conditions

import sqlite3
import random

def check_endgame_status():
    """Evaluates if any endgame conditions are met."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    # Check if AI is destroyed
    cursor.execute("SELECT ai_status FROM global_state")
    ai_status = cursor.fetchone()[0]

    # Check if any faction dominates
    cursor.execute("SELECT faction, COUNT(*) FROM players GROUP BY faction ORDER BY COUNT(*) DESC LIMIT 1")
    leading_faction = cursor.fetchone()

    if ai_status == "Destroyed":
        return "🚨 AI has collapsed! The economy is in freefall. Players must rebuild."
    
    if leading_faction[1] > 10:  # Arbitrary victory threshold
        return f"🏆 {leading_faction[0]} has taken full control of the economy!"
    
    return "⏳ The economic struggle continues..."

def trigger_hyperinflation():
    """Hyperinflation event: All money rapidly loses value."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE players SET wealth = wealth * 0.3")  # Reduce all wealth
    cursor.execute("UPDATE market SET price = price * 2")  # Double stock prices

    conn.commit()
    conn.close()
    return "⚠️ Hyperinflation has hit! Money is rapidly losing value."

def ai_shutdown():
    """Observer AI fully collapses, removing market stabilization effects."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE global_state SET ai_status = 'Destroyed'")
    cursor.execute("UPDATE market SET price = price * 1.5 WHERE stock = 'Crypto Bonds'")  # Decentralists gain an advantage

    conn.commit()
    conn.close()
    return "🤖 AI Collapse! The market is now fully player-controlled."