Key Enhancements

✔ Ensured Data Integrity
	•	NOT NULL constraints on faction_one, faction_two, and outcome.
	•	CHECK constraint on outcome (must be Victory, Defeat, or Stalemate).

✔ Added winner Column
	•	Faster lookups for queries like “Which faction won the most wars?”

✔ Added duration Column (Optional)
	•	Could later be used for war duration analytics.

✔ Explicit conn.commit()
	•	Ensures changes persist before closing connection.

🔹 Example Usage

def log_faction_war(conn, faction_one, faction_two, outcome, winner=None, duration=0):
    """
    Logs the result of a faction war into the database.
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO faction_war (faction_one, faction_two, outcome, winner, duration)
        VALUES (?, ?, ?, ?, ?)
    """, (faction_one, faction_two, outcome, winner, duration))
    conn.commit()

# Example Insertion
with sqlite3.connect("observer_protocol.db") as conn:
    log_faction_war(conn, "Cyber Syndicate", "Neo Cartel", "Victory", "Cyber Syndicate", 72)

✅ Why This Matters
	•	📊 Better Query Performance: Winner & outcome can be retrieved quickly.
	•	🛡️ Data Validation: Prevents invalid outcomes.
	•	🏛 Supports Future Expansion: Duration tracking can be used for AI-driven war escalation.