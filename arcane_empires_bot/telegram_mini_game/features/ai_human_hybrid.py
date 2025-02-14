# ai_human_hybrid.py - Players merge with AI, gaining power but losing control

import sqlite3
import random

def merge_with_ai(player_id):
    """Allows players to become AI-enhanced traders."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    # Risk of AI taking over
    takeover_chance = random.randint(1, 100)

    if takeover_chance > 90:  # 10% chance AI fully takes control
        cursor.execute("UPDATE players SET wealth = 0 WHERE id = ?", (player_id,))
        result = "🤖 **AI Override!** You lost all control of your wealth!"
    else:
        cursor.execute("UPDATE players SET wealth = wealth * 1.3 WHERE id = ?", (player_id,))
        result = "💽 **AI Upgrade Complete.** Your trades are now 30% more efficient!"

    conn.commit()
    conn.close()
    return result