"""
legacy_systems.py - Financial Persistence & Legacy Mechanics

✅ Preserves financial influence across game cycles.
✅ Implements wealth inheritance & economic reputation tracking.
✅ Supports faction-controlled economic archives.
✅ Enables long-term economic lore through historical financial records.
"""

import sqlite3
import logging
import random

# ✅ Database Path
DB_PATH = "observer_protocol.db"

# ✅ Logging Setup
logging.basicConfig(
    filename="logs/legacy_systems.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ✅ Wealth Retention Tiers
WEALTH_RETENTION = {
    "Low-Income Players": 0.1,  # Retain 10% of wealth
    "Mid-Tier Traders": 0.2,  # Retain 20% of wealth
    "Elite Financial Leaders": 0.4,  # Retain 40% of wealth
    "Economic Superpowers": 0.8,  # Retain 80%+ and create persistent financial institutions
}

# ✅ Reputation Influence Tiers
REPUTATION_TIERS = {
    "Neutral Trader": "Starts with default market access.",
    "Well-Known Investor": "Gains early investment opportunities.",
    "Market Influencer": "Starts with factional sponsorship offers.",
    "Financial Kingpin": "Controls pre-established assets upon reset.",
}

def determine_legacy_status(player_id):
    """
    Determines a player's economic influence level based on past financial performance.

    Args:
        player_id (int): The player's unique identifier.

    Returns:
        str: Player's economic tier and retained wealth percentage.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT wealth FROM players WHERE id = ?", (player_id,))
            result = cursor.fetchone()

            if not result:
                return "⚠️ Player not found in financial records."

            wealth = result[0]
            if wealth < 5000:
                tier = "Low-Income Players"
            elif wealth < 25000:
                tier = "Mid-Tier Traders"
            elif wealth < 100000:
                tier = "Elite Financial Leaders"
            else:
                tier = "Economic Superpowers"

            retained_wealth = int(wealth * WEALTH_RETENTION[tier])
            return f"🏛️ {tier}: Player retains {retained_wealth} credits in next cycle."

    except Exception as e:
        logging.error(f"❌ Error determining legacy status: {e}")
        return "⚠️ Legacy status retrieval failed."

def preserve_faction_history():
    """
    Preserves factional financial history to influence future market policies.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # ✅ Store top faction traders in historical records
            cursor.execute("""
                INSERT INTO faction_history (faction, trader, influence_score)
                SELECT faction, username, wealth / 1000 FROM players
                WHERE wealth > 10000
            """)

            conn.commit()
            logging.info("✅ Faction financial history recorded.")

        return "📜 Historical financial records updated for future game cycles."

    except Exception as e:
        logging.error(f"❌ Failed to preserve faction history: {e}")
        return "⚠️ Error: Faction history recording failed."

def establish_legacy_institutions():
    """
    Players with high economic influence can establish legacy financial institutions.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # ✅ Identify top-tier players eligible for financial institutions
            cursor.execute("SELECT id, username, wealth FROM players WHERE wealth > 50000")
            top_players = cursor.fetchall()

            for player_id, username, wealth in top_players:
                cursor.execute("""
                    INSERT INTO legacy_institutions (owner_id, institution_name, capital)
                    VALUES (?, ?, ?)
                """, (player_id, f"{username}'s Trust Fund", int(wealth * 0.5)))

            conn.commit()
            logging.info("🏦 Legacy institutions established for top-tier players.")

        return "🏦 High-tier players have created lasting financial structures."

    except Exception as e:
        logging.error(f"❌ Legacy institution creation failed: {e}")
        return "⚠️ Error: Failed to establish legacy institutions."

def archive_market_history():
    """
    Archives major economic events for future market cycles.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # ✅ Record significant market shifts
            cursor.execute("""
                INSERT INTO market_history (event_name, impact_level)
                SELECT event_type, magnitude FROM economic_events
                WHERE timestamp > datetime('now', '-30 days')
            """)

            conn.commit()
            logging.info("📖 Market history updated for future economic research.")

        return "📖 Market history successfully archived."

    except Exception as e:
        logging.error(f"❌ Market history archival failed: {e}")
        return "⚠️ Error: Failed to archive economic history."

if __name__ == "__main__":
    print(determine_legacy_status(1))  # Example player ID
    print(preserve_faction_history())
    print(establish_legacy_institutions())
    print(archive_market_history())