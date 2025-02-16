import os
import random
import sqlite3
from datetime import datetime, timedelta

# 🔹 Database path (modify if needed)
DB_PATH = "/workspaces/mini-app/observer_protocol.db"

# 🔹 Stocks AI can trade
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Arcane Bonds"]

# 🔹 Bull/Bear Market Influence
MARKET_PHASES = ["Bull", "Bear"]

# 🔹 AI Trading Risk Profiles
AI_PROFILES = {
    "Conservative": {"buy_chance": 30, "sell_chance": 70, "risk_tolerance": 10},
    "Balanced": {"buy_chance": 50, "sell_chance": 50, "risk_tolerance": 25},
    "Aggressive": {"buy_chance": 70, "sell_chance": 30, "risk_tolerance": 50},
}

# 🔹 AI Trading Behavior
def get_ai_profile():
    """Randomly selects an AI trading profile based on market conditions."""
    phase = get_market_phase()
    if phase == "Bull":
        return AI_PROFILES["Aggressive"]
    else:
        return AI_PROFILES["Conservative"]

def get_market_phase():
    """Determines current market phase (Bull or Bear)."""
    return random.choice(MARKET_PHASES)

def get_stock_trend(stock):
    """Analyzes short-term price trends for AI decision-making."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM market WHERE stock = ? ORDER BY timestamp DESC LIMIT 5", (stock,))
    prices = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    if len(prices) < 5:
        return "Neutral"
    
    if prices[0] > prices[-1]:  # Price is rising
        return "Uptrend"
    elif prices[0] < prices[-1]:  # Price is falling
        return "Downtrend"
    return "Stable"

def ai_trade():
    """AI decides to buy or sell based on market conditions."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    ai_profile = get_ai_profile()
    print(f"🤖 AI Trading Profile: {ai_profile}")

    for stock in STOCKS:
        trend = get_stock_trend(stock)
        decision = random.randint(1, 100)

        if trend == "Uptrend" and decision <= ai_profile["buy_chance"]:
            trade_amount = random.randint(10, ai_profile["risk_tolerance"])
            cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (trade_amount, stock))
            print(f"📈 AI Buys {stock}: +{trade_amount} credits")

        elif trend == "Downtrend" and decision <= ai_profile["sell_chance"]:
            trade_amount = random.randint(10, ai_profile["risk_tolerance"])
            cursor.execute("UPDATE market SET price = price - ? WHERE stock = ?", (trade_amount, stock))
            print(f"📉 AI Sells {stock}: -{trade_amount} credits")

    conn.commit()
    conn.close()

def detect_exploit_stock():
    """Detects if a stock's price has changed too fast and flags for manipulation."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT stock, MAX(price) - MIN(price) FROM market WHERE timestamp >= datetime('now', '-1 day')")
    anomalies = cursor.fetchall()
    conn.close()
    
    flagged_stocks = [stock for stock, change in anomalies if change > 50]  # Threshold for manipulation
    if flagged_stocks:
        print(f"🚨 Possible Market Exploits Detected: {flagged_stocks}")

def ai_market_update():
    """AI updates its trading behavior and detects manipulation."""
    ai_trade()
    detect_exploit_stock()

if __name__ == "__main__":
    ai_market_update()