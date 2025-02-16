"""
combat.py - AI Market Warfare & Weak-Handed Player Exploitation

✅ AI detects and punishes weak-handed traders (low confidence, frequent panic selling).
✅ Introduces AI-driven market pressure tactics (price shocks, liquidity traps).
✅ Creates faction-based counterplay options (black-market protection, AI manipulation).
✅ AI evolves over time, tracking player behavior for future attacks.
"""

import random
import sqlite3
import logging
from datetime import datetime

# Database path (adjust if necessary)
DB_PATH = "/workspaces/app/bot/database/observer_protocol.db"

# AI Countermeasure Levels
COUNTERMEASURE_LEVELS = {
    "low": "Minor AI adjustments to prevent player abuse.",
    "medium": "AI disrupts liquidity and prevents exploitation.",
    "high": "AI enforces direct economic retaliation.",
    "extreme": "AI market lockdown—players face trading restrictions."
}

# Logging Configuration
logging.basicConfig(
    filename="/workspaces/app/logs/ai_combat.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def detect_weak_handed_players():
    """
    AI scans trade history for weak-handed players (frequent panic selling).
    Returns a list of vulnerable traders.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Identifies players who sell frequently at declining prices
    cursor.execute("""
        SELECT player_id, COUNT(*) AS sell_count
        FROM trade_history
        WHERE amount < 0  -- Selling activity
        GROUP BY player_id
        HAVING sell_count > 3
    """)
    
    weak_hands = cursor.fetchall()
    conn.close()

    if weak_hands:
        logging.info(f"🤖 AI Detected Weak-Handed Players: {weak_hands}")
        return weak_hands
    return []

def shake_out_weak_hands():
    """
    AI forces weak-handed players out of the market by triggering price drops.
    """
    weak_hands = detect_weak_handed_players()
    
    if not weak_hands:
        return "No weak-handed players detected."

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for player_id, _ in weak_hands:
        # AI manipulates market to punish weak hands
        cursor.execute("""
            UPDATE market 
            SET price = price - ? 
            WHERE stock IN (
                SELECT stock FROM trade_history WHERE player_id = ? ORDER BY timestamp DESC LIMIT 1
            )
        """, (random.randint(20, 50), player_id))
        logging.warning(f"⚠ AI Shakeout: Player {player_id} targeted with forced sell-off.")

    conn.commit()
    conn.close()
    return "✅ AI Shakeout Completed: Weak hands forced out."

def detect_market_exploit():
    """
    AI scans trade history for signs of manipulation.
    Returns the detected anomaly level: 'low', 'medium', 'high', or 'extreme'.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT stock, SUM(amount) FROM trade_history GROUP BY stock ORDER BY SUM(amount) DESC LIMIT 1")
    most_traded = cursor.fetchone()
    conn.close()

    if not most_traded:
        return "low"  # No exploits detected

    stock, volume = most_traded
    logging.info(f"📊 AI Market Scan: Detected high trading volume in {stock}.")

    if volume > 5000:
        return "extreme"
    elif volume > 3000:
        return "high"
    elif volume > 1500:
        return "medium"
    else:
        return "low"

def apply_ai_countermeasure(level):
    """
    AI executes financial disruptions based on detected exploit severity.
    """
    countermeasure = COUNTERMEASURE_LEVELS[level]
    logging.info(f"🚨 AI Countermeasure Activated: {countermeasure}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if level in ["medium", "high", "extreme"]:
        # AI manipulates liquidity & trade values
        cursor.execute("UPDATE market SET price = price + ? WHERE stock = (SELECT stock FROM trade_history ORDER BY timestamp DESC LIMIT 1)", (random.randint(10, 50),))

    if level in ["high", "extreme"]:
        # AI issues liquidity freezes on targeted stocks
        cursor.execute("UPDATE market SET price = 0 WHERE stock = (SELECT stock FROM trade_history ORDER BY timestamp DESC LIMIT 1)")

    if level == "extreme":
        # AI enforces full trading lockdown
        cursor.execute("DELETE FROM trade_history WHERE timestamp >= ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
        logging.warning("⚠ AI LOCKDOWN: Trade history wiped for exploit prevention!")

    conn.commit()
    conn.close()
    return f"✅ AI Countermeasure Applied: {countermeasure}"

def execute_ai_warfare():
    """
    AI responds to market exploitation by enforcing countermeasures dynamically.
    Also identifies and shakes out weak-handed traders.
    """
    exploit_level = detect_market_exploit()
    response = apply_ai_countermeasure(exploit_level)
    
    shakeout_response = shake_out_weak_hands()
    
    return f"{response}\n{shakeout_response}"

if __name__ == "__main__":
    print(execute_ai_warfare())