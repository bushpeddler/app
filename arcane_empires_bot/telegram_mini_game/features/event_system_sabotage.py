"""
event_system_sabotage.py - Handles AI-triggered events related to stock crashes, economic warfare, and sabotage.

This module selects a random sabotage-type market event and applies the corresponding market updates.
"""

import random
import sqlite3

EVENTS = [
    "🛑 AI Market Crash! All stocks drop by 30%.",
    "🚀 Syndicate Black Market Surge! Certain assets increase 50%.",
    "⚠️ AI Overload: Automated trading algorithms cause unpredictable swings.",
    "🔄 Faction War: Technocrats stabilize economy while Syndicate exploits panic."
]

def trigger_event():
    """
    Triggers a random sabotage-type market event and applies corresponding database updates.

    - "Crash": Reduces all stock prices by 30%.
    - "Surge": Increases the price of 'Quantum Energy' by 50%.
    - "AI Overload": Increases the price of 'NeoTech AI' by 10 credits.
    - "Faction War": No direct market update is applied.

    Returns:
        str: The description of the triggered event.
    """
    event = random.choice(EVENTS)

    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        
        if "Crash" in event:
            cursor.execute("UPDATE market SET price = price * 0.7")
        elif "Surge" in event:
            cursor.execute("UPDATE market SET price = price * 1.5 WHERE stock = ?", ("Quantum Energy",))
        elif "AI Overload" in event:
            cursor.execute("UPDATE market SET price = price + 10 WHERE stock = ?", ("NeoTech AI",))
        # Note: "Faction War" event does not trigger any direct market update in this version.
        
        conn.commit()
    
    return event