# asset_bubbles.py - AI inflates asset prices before collapsing them

import sqlite3
import random

BUBBLE_STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits"]

def generate_bubble():
    """AI artificially inflates an asset before a future crash."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    stock = random.choice(BUBBLE_STOCKS)
    cursor.execute("UPDATE market SET price = price * 2 WHERE stock = ?", (stock,))
    
    conn.commit()
    conn.close()
    return f"🔥 **Asset Bubble Detected!** {stock} price **doubled**, but may crash soon!"

def crash_bubble():
    """AI crashes a previously inflated stock, wiping its value."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    stock = random.choice(BUBBLE_STOCKS)
    cursor.execute("UPDATE market SET price = price * 0.4 WHERE stock = ?", (stock,))
    
    conn.commit()
    conn.close()
    return f"💥 **Market Crash!** {stock} lost **60% of its value overnight!**"