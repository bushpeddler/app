# market_engine.py - AI-driven stock market engine with configurable behavior

import random
import sqlite3
import faction_system

# Configuration flags for different market behaviors
ENABLE_FACTION_INFLUENCE = True
ENABLE_AI_TRADE_ANALYSIS = True

# Define a common list of stocks
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Crypto Bonds"]

def get_market_status():
    """Returns current stock values."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM market")
    data = cursor.fetchall()
    conn.close()
    return {stock[0]: stock[1] for stock in data}

def update_market():
    """
    Simulates AI-driven market price changes.
    
    - Always applies random fluctuations.
    - Optionally includes faction-based influences.
    - Optionally applies AI trade analysis based on recent trades.
    """
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    # Apply basic random fluctuations to all stocks
    for stock in STOCKS:
        change = random.randint(-20, 50)
        cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (change, stock))

    # If enabled, adjust market based on recent player trades (AI analysis)
    if ENABLE_AI_TRADE_ANALYSIS:
        cursor.execute("SELECT * FROM trade_history ORDER BY timestamp DESC LIMIT 5")
        recent_trades = cursor.fetchall()
        for trade in recent_trades:
            stock, amount = trade[1], trade[2]
            if amount > 500:  # Large transactions increase price
                cursor.execute("UPDATE market SET price = price + 30 WHERE stock = ?", (stock,))
            else:  # Smaller trades reduce price slightly
                cursor.execute("UPDATE market SET price = price - 10 WHERE stock = ?", (stock,))

    # If enabled, incorporate faction influence into market trends
    if ENABLE_FACTION_INFLUENCE:
        cursor.execute("SELECT DISTINCT id FROM players WHERE faction IS NOT NULL")
        faction_players = cursor.fetchall()
        for player in faction_players:
            # The function manipulate_market() can perform additional adjustments
            faction_system.manipulate_market(player[0])

    conn.commit()
    conn.close()

def ai_trades():
    """
    Alternative function: AI analyzes a broader set of recent trades
    and applies market adjustments. Can be used separately or integrated
    within update_market().
    """
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trade_history ORDER BY timestamp DESC LIMIT 10")
    recent_trades = cursor.fetchall()

    for trade in recent_trades:
        stock, amount = trade[1], trade[2]
        if amount > 500:
            cursor.execute("UPDATE market SET price = price + 30 WHERE stock = ?", (stock,))
        else:
            cursor.execute("UPDATE market SET price = price - 10 WHERE stock = ?", (stock,))

    conn.commit()
    conn.close()