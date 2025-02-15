import random
import sqlite3

# List of stocks used in the basic market simulation
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Arcane Bonds"]

def get_market_status():
    """Returns current stock values from the market table."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM market")
    data = cursor.fetchall()
    conn.close()
    return {stock[0]: stock[1] for stock in data}

def update_market(stock, amount):
    """
    Updates market prices based on trade volume.
    
    Parameters:
    stock (str): The name of the stock to update.
    amount (int): The amount of the stock traded, influencing the price change.
    """
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()
    
    # Modify stock price dynamically based on the amount traded
    if amount > 500:
        change = 30  # Increase price if trade amount is high
    else:
        change = random.randint(-20, 10)  # Random change if trade amount is low, with a bias towards decrease
    
    cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (change, stock))
    conn.commit()
    conn.close()
    
    print(f"📈 Updated {stock}: {change} credits (Traded Amount: {amount})")  # ✅ Debugging Log

def ai_trades():
    """
    Analyzes recent player trades and adjusts stock prices accordingly.
    - If a trade amount exceeds 500, the price is increased by 30.
    - Otherwise, the price is decreased by a random value between -20 and 10.
    """
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trade_history ORDER BY timestamp DESC LIMIT 10")
    recent_trades = cursor.fetchall()
    
    for trade in recent_trades:
        stock, amount = trade[1], trade[2]
        update_market(stock, amount)
    
    conn.close()
    
    print("✅ AI Trade Adjustments Complete")  # ✅ Debugging Log