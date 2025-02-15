# unlock_system.py - Unlocks advanced game mechanics based on player progression

import sqlite3

# Unlock thresholds (adjustable for balance)
UNLOCK_THRESHOLDS = {
    "Phase 2": {"trades": 10, "faction_influence": 3},  # Unlock AI market manipulation
    "Phase 3": {"trades": 30, "wealth": 5000},  # Unlock black market, AI-human trading
    "Phase 4": {"trades": 60, "ai_morality": "Exploitative"},  # AI Override & Endgame Events
}

def check_progress(player_id):
    """Checks player progress and determines if a new phase should unlock."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    # Fetch player stats
    cursor.execute("SELECT COUNT(*) FROM trade_history WHERE player_id = ?", (player_id,))
    total_trades = cursor.fetchone()[0]

    cursor.execute("SELECT wealth FROM players WHERE id = ?", (player_id,))
    player_wealth = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM players WHERE faction IS NOT NULL")
    faction_influence = cursor.fetchone()[0]

    cursor.execute("SELECT ai_morality FROM global_state")
    ai_morality = cursor.fetchone()[0]

    conn.close()

    # Determine unlock phase
    if total_trades >= UNLOCK_THRESHOLDS["Phase 4"]["trades"] and ai_morality == "Exploitative":
        return "Phase 4"
    elif total_trades >= UNLOCK_THRESHOLDS["Phase 3"]["trades"] and player_wealth >= UNLOCK_THRESHOLDS["Phase 3"]["wealth"]:
        return "Phase 3"
    elif total_trades >= UNLOCK_THRESHOLDS["Phase 2"]["trades"] and faction_influence >= UNLOCK_THRESHOLDS["Phase 2"]["faction_influence"]:
        return "Phase 2"
    
    return "Phase 1"  # Default starting phase