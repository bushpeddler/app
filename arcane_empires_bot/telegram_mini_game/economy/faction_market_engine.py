import random
import sqlite3
import faction_system

# List of stocks used in the faction-influenced market simulation
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Crypto Bonds"]

def get_market_status():
    """Returns current stock values from the market table."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM market")
    data = cursor.fetchall()
    conn.close()
    return {stock[0]: stock[1] for stock in data}

def update_market():
    """
    Simulates AI-driven market price changes with faction-based influence.
    
    - Applies basic random fluctuations to each stock.
    - Reviews recent trade history to adjust prices:
      - Increases price by 30 for large transactions (amount > 500).
      - Decreases price by 10 for smaller trades.
    - Incorporates faction influence by triggering market manipulation for each player with a faction.
    """
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    # Apply basic random fluctuations
    for stock in STOCKS:
        change = random.randint(-20, 50)
        cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (change, stock))
    
    # AI reaction based on recent trades
    cursor.execute("SELECT * FROM trade_history ORDER BY timestamp DESC LIMIT 5")
    recent_trades = cursor.fetchall()
    for trade in recent_trades:
        stock, amount = trade[1], trade[2]
        if amount > 500:
            cursor.execute("UPDATE market SET price = price + 30 WHERE stock = ?", (stock,))
        else:
            cursor.execute("UPDATE market SET price = price - 10 WHERE stock = ?", (stock,))
    
    # Incorporate faction influence
    cursor.execute("SELECT DISTINCT id FROM players WHERE faction IS NOT NULL")
    faction_players = cursor.fetchall()
    for player in faction_players:
        faction_system.manipulate_market(player[0])
    
    conn.commit()
    conn.close()