"""
ai_trading_logic.py - AI-Driven Market Interaction

This module governs AI trading behavior in the market, reacting to:
- Market volatility
- Player trading trends
- Faction-based economy shifts
- AI-led trading anomalies

🔹 AI Trading Features:
✅ Analyzes market trends & adjusts stock values.
✅ Reacts to high-frequency player trades.
✅ Can trigger automated investment strategies.
✅ Influences AI-generated financial shifts.
"""

import random
import sqlite3
import logging
from market.engine import update_market, get_market_status

# Database path (adjust if necessary)
DB_PATH = "/workspaces/app/bot/database/observer_protocol.db"

# AI Investor Profiles
AI_PROFILES = {
    "Cautious Investor": {"risk_tolerance": 0.3, "investment_rate": 0.2},
    "Aggressive Trader": {"risk_tolerance": 0.8, "investment_rate": 0.7},
    "Market Manipulator": {"risk_tolerance": 1.0, "investment_rate": 0.9},
}

# Setup Logging
logging.basicConfig(
    filename="/workspaces/app/logs/ai_trading.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def get_recent_trades():
    """
    Retrieves the last 10 trades to analyze market activity.

    Returns:
        list: Recent trade data in [(stock, amount, trader_type)] format.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT stock, amount, trader_type FROM trade_history ORDER BY timestamp DESC LIMIT 10")
    trades = cursor.fetchall()
    conn.close()
    return trades

def ai_trade_decision():
    """
    AI traders analyze recent trades & decide on their next market action.

    AI will:
    - Adjust stock values based on risk tolerance.
    - Make random high-frequency trades.
    - React dynamically to player activity.
    """
    market_data = get_market_status()
    trades = get_recent_trades()

    for ai_name, profile in AI_PROFILES.items():
        for stock, amount, trader_type in trades:
            if trader_type == "AI":
                continue  # Skip AI self-trading to prevent infinite loops

            risk = profile["risk_tolerance"]
            investment = profile["investment_rate"]

            # AI DECISION: Increase price if player trade is high-volume
            if amount > 500:
                price_change = int(amount * investment * risk)
            else:
                price_change = random.randint(-10, 20)  # Random market movement

            # Execute AI Market Response
            update_market(stock, price_change)
            logging.info(f"🤖 {ai_name} adjusted {stock} by {price_change} credits.")

    return "✅ AI Trading Adjustments Applied."

if __name__ == "__main__":
    print(ai_trade_decision())