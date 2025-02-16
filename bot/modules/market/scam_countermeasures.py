# scam_countermeasures.py - Allows players to buy scam protection

import sqlite3

DB_PATH = "observer_protocol.db"

def has_scam_protection(player_id):
    """Checks if a player has active scam countermeasures."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM scam_protection WHERE player_id = ?", (player_id,))
    result = cursor.fetchone()
    conn.close()
    return bool(result)

def buy_scam_protection(player_id):
    """Allows a player to buy scam countermeasures."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Deduct currency for purchasing scam detection
    cursor.execute("UPDATE players SET wealth = wealth - 500 WHERE id = ?", (player_id,))
    
    # Add protection status
    cursor.execute("INSERT INTO scam_protection (player_id) VALUES (?)", (player_id,))
    
    conn.commit()
    conn.close()

    return "🛡️ Scam protection purchased! AI manipulations will now be detected."