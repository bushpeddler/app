import os
import random
import sqlite3

# Define database path dynamically
DB_PATH = os.path.join(os.path.dirname(__file__), "../observer_protocol.db")

# List of stocks used in the market simulation
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Arcane Bonds"]

def get_market_status():
    """Fetches current stock values from the market table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT stock, price FROM market")
    data = cursor.fetchall()
    conn.close()
    return {stock: price for stock, price in data}

def update_market():
    """
    Simulates AI-driven market price changes with random fluctuations.
    Each stock's price is adjusted by a random value between -20 and 50.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for stock in STOCKS:
        change = random.randint(-20, 50)
        cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (change, stock))

    conn.commit()
    conn.close()

def ai_trades():
    """
    Analyzes recent player trades and adjusts stock prices.
    - If a trade amount exceeds 500, the price increases by 30.
    - Otherwise, the price decreases by 10.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT stock, amount FROM trade_history ORDER BY timestamp DESC LIMIT 10")
    recent_trades = cursor.fetchall()

    for stock, amount in recent_trades:
        if amount > 500:
            cursor.execute("UPDATE market SET price = price + 30 WHERE stock = ?", (stock,))
        else:
            cursor.execute("UPDATE market SET price = price - 10 WHERE stock = ?", (stock,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Current Market Status:", get_market_status())
    update_market()
    ai_trades()
    print("Market Updated.")