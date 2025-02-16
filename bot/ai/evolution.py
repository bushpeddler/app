# ai_evolution.py - AI learns from past trends and counters player strategies

import sqlite3
import random
import logging

# Database Path
DB_PATH = "/workspaces/app/bot/database/observer_protocol.db"

# AI Market Strategy Adjustments
PRICE_ADJUSTMENT_CAP = 100  # Max AI can change a stock price per cycle
ADJUSTMENT_FACTOR = 0.05  # AI adjusts price based on trade volume

# Setup Logging
logging.basicConfig(
    filename="/workspaces/app/logs/ai_evolution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def analyze_player_trends():
    """AI studies trade patterns to counteract player influence on the market."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch top traded stocks (AI prioritizes highly traded assets)
    cursor.execute("""
        SELECT stock, SUM(amount) 
        FROM trade_history 
        GROUP BY stock 
        ORDER BY SUM(amount) DESC 
        LIMIT 3
    """)
    traded_stocks = cursor.fetchall()

    if not traded_stocks:
        logging.info("📉 No recent trades detected. AI takes no action.")
        conn.close()
        return "⚠️ No market activity detected. AI did not adjust the market."

    ai_adjustments = []
    for stock, volume in traded_stocks:
        price_adjustment = min(int(volume * ADJUSTMENT_FACTOR), PRICE_ADJUSTMENT_CAP)  # Prevents over-inflation

        cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (price_adjustment, stock))
        ai_adjustments.append(f"{stock}: {price_adjustment} credits")

    conn.commit()
    conn.close()

    log_message = f"🤖 AI detected high trading volume! Adjustments: {', '.join(ai_adjustments)}"
    logging.info(log_message)
    return log_message

if __name__ == "__main__":
    print(analyze_player_trends())