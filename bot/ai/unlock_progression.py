def check_progress(player_id):
    """
    Determines the current game phase based on player actions and global economic conditions.

    Args:
        player_id (int): The player's unique identifier.

    Returns:
        str: The current game phase.
    """
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()

        # Check total wealth & market influence
        cursor.execute("SELECT wealth FROM players WHERE id = ?", (player_id,))
        wealth = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM trade_history WHERE player_id = ?", (player_id,))
        total_trades = cursor.fetchone()[0]

        # Unlock phases dynamically
        if wealth >= 50000 and total_trades > 50:
            return "Phase 4: Endgame Events"
        elif wealth >= 20000 and total_trades > 30:
            return "Phase 3: High-Risk Economy"
        elif wealth >= 5000 and total_trades > 10:
            return "Phase 2: Advanced Economy"
        else:
            return "Phase 1: Early Game"

# Example Usage
player_phase = check_progress(1)
print(f"📊 Current Phase: {player_phase}")