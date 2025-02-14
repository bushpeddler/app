"""
event_system_collapse.py - Handles AI-triggered events related to market crises, economic warfare, and collapse.

This module triggers random market crises and applies corresponding database updates,
including drastic market shifts and invoking endgame scenarios.
"""

import random
import sqlite3
import endgame_scenarios

EVENTS = [
    "📉 Market Collapse: AI miscalculates, all stocks lose 40% value.",
    "🛑 AI Lockdown: Observer AI halts trading temporarily.",
    "🚀 Hyperinflation: All wealth devalues, forcing drastic market shifts.",
    "⚔️ Faction War: Syndicate vs. Technocrats fight for control."
]

def trigger_event():
    """
    Triggers a random market crisis event and applies corresponding updates.

    - "Market Collapse": Reduces all stock prices by 40%.
    - "AI Lockdown": Applies a 10% dip in all stock prices.
    - "Hyperinflation": Invokes an endgame scenario for hyperinflation.
    - "Faction War": Increases the price of 'Shadow Bank' by 20%.

    Returns:
        str: The description of the triggered event.
    """
    event = random.choice(EVENTS)

    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        
        if "Market Collapse" in event:
            cursor.execute("UPDATE market SET price = price * 0.6")
        elif "AI Lockdown" in event:
            cursor.execute("UPDATE market SET price = price * 0.9")
        elif "Hyperinflation" in event:
            # This event triggers a more complex endgame scenario.
            endgame_scenarios.trigger_hyperinflation()
        elif "Faction War" in event:
            cursor.execute("UPDATE market SET price = price * 1.2 WHERE stock = ?", ("Shadow Bank",))
        
        conn.commit()
    
    return event