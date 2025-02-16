# multi_stock_scam.py - AI manipulates multiple assets simultaneously

import sqlite3
import random

DB_PATH = "observer_protocol.db"
SCAM_STOCKS = ["Quantum Energy", "NeoTech AI", "Shadow Bank"]

def trigger_multi_stock_scam(player_id):
    """AI manipulates multiple stock prices at the same time."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for stock in SCAM_STOCKS:
        if random.randint(1, 100) > 50:  # 50% chance per stock
            cursor.execute("UPDATE market SET price = price * 1.5 WHERE stock = ?", (stock,))

    conn.commit()
    conn.close()

    return "📈 AI-triggered multi-stock manipulation detected!"