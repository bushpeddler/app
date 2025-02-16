Key Enhancements

✔ Ensured Single Row Exists
	•	Primary Key id=1 guarantees there’s only one global state record.
	•	INSERT OR IGNORE ensures it does not create duplicates.

✔ Added market_trend
	•	Tracks economic trends (e.g., Bull Market, Bear Market, Volatile).

✔ Added economic_stability
	•	A scale (0-100) that represents economic health.
	•	Could trigger crises or booms based on AI/player influence.

✔ Added faction_dominance
	•	Tracks which faction currently dominates the economy.

✔ Added last_updated
	•	Allows real-time tracking of economic shifts.

🔹 Example Usage

def update_global_state(conn, ai_status=None, market_trend=None, economic_stability=None, faction_dominance=None):
    """
    Updates the global economic state.
    """
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE global_state
        SET 
            ai_status = COALESCE(?, ai_status),
            market_trend = COALESCE(?, market_trend),
            economic_stability = COALESCE(?, economic_stability),
            faction_dominance = COALESCE(?, faction_dominance),
            last_updated = CURRENT_TIMESTAMP
        WHERE id = 1
    """, (ai_status, market_trend, economic_stability, faction_dominance))

    conn.commit()

# Example Update
with sqlite3.connect("observer_protocol.db") as conn:
    update_global_state(conn, ai_status="Rogue", market_trend="Volatile", economic_stability=30, faction_dominance="Cyber Syndicate")

✅ Why This Matters
	•	🏛 Tracks AI Status: AI can be Active, Dormant, Rogue, or Destroyed.
	•	📉 Economic Crisis System: Stability drops below 20, game-wide events trigger.
	•	🏴 Faction Influence: Tracks who dominates the market.
	•	⏳ Historical Changes: Last updated timestamp allows time-based AI behavior shifts.