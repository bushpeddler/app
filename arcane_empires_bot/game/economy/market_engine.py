import os
import random
import sqlite3

# Correct database path
DB_PATH = "/workspaces/mini-app/observer_protocol.db"

# List of stocks used in the basic market simulation
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Arcane Bonds"]

def get_market_status():
    """Returns current stock values from the market table."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM market")
        data = cursor.fetchall()
        conn.close()
        return {stock[0]: stock[1] for stock in data}
    except sqlite3.Error as e:
        print(f"❌ Database Error: {e}")
        return {}

def update_market():
    """
    Simulates AI-driven market price changes with basic random fluctuations.
    Each stock's price is adjusted by a random value between -20 and 50.
    Ensures stock exists before updating.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        for stock in STOCKS:
            cursor.execute("SELECT 1 FROM market WHERE stock = ?", (stock,))
            if cursor.fetchone():  # Ensures stock exists before updating
                change = random.randint(-20, 50)
                cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (change, stock))
                print(f"📈 Updated {stock}: {change} credits")
            else:
                print(f"⚠️ Stock '{stock}' not found in the market table.")

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"❌ Database Error: {e}")

def ai_trades():
    """
    Analyzes recent player trades and adjusts stock prices accordingly.
    - If a trade amount exceeds 500, the price is increased by 30.
    - Otherwise, the price is decreased by 10.
    - Ensures the traded stock exists before updating.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trade_history ORDER BY timestamp DESC LIMIT 10")
        recent_trades = cursor.fetchall()

        for trade in recent_trades:
            stock, amount = trade[1], trade[2]

            # Ensure stock exists before updating
            cursor.execute("SELECT 1 FROM market WHERE stock = ?", (stock,))
            if cursor.fetchone():
                if amount > 500:
                    cursor.execute("UPDATE market SET price = price + 30 WHERE stock = ?", (stock,))
                    print(f"📈 AI Trade: {stock} increased by 30 credits")
                else:
                    cursor.execute("UPDATE market SET price = price - 10 WHERE stock = ?", (stock,))
                    print(f"📉 AI Trade: {stock} decreased by 10 credits")
            else:
                print(f"⚠️ AI Trade Skipped: '{stock}' does not exist in the market table.")

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"❌ Database Error: {e}")