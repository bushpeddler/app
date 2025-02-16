# ai_evolution.py - AI learns from past trends and counters player strategies

import sqlite3
import random

def analyze_player_trends():
    """AI studies past trade patterns to counteract player manipulation."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    cursor.execute("SELECT stock, SUM(amount) FROM trade_history GROUP BY stock ORDER BY SUM(amount) DESC LIMIT 1")
    most_traded_stock = cursor.fetchone()

    if most_traded_stock:
        stock, volume = most_traded_stock
        price_adjustment = int(volume * 0.05)  # AI increases prices on highly traded assets
        cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (price_adjustment, stock))

    conn.commit()
    conn.close()
    return f"🤖 AI detected high trading volume in {stock}! Market adjusted."