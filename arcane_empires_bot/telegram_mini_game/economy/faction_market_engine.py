import random
import sqlite3
from economy import faction_system  # ✅ Ensure correct import

# List of stocks used in the faction-influenced market simulation
STOCKS = ["Quantum Energy", "NeoTech AI", "Cyber Credits", "Shadow Bank", "Crypto Bonds"]

def get_market_status():
    """Returns current stock values from the market table."""
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT stock, price FROM market")
        data = cursor.fetchall()
    return {stock: price for stock, price in data}

def update_market():
    """
    Simulates AI-driven market price changes with faction-based influence.

    - Applies basic random fluctuations to each stock.
    - Reviews recent trade history to adjust prices:
      - Increases price for large transactions.
      - Decreases price for smaller trades.
    - Incorporates faction influence by triggering market manipulation.
    """
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()

        # Apply basic random fluctuations
        for stock in STOCKS:
            change = random.randint(-20, 50)
            cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (change, stock))
        
        # AI reaction based on recent trades
        cursor.execute("SELECT stock, amount FROM trade_history ORDER BY timestamp DESC LIMIT 5")
        recent_trades = cursor.fetchall()
        for stock, amount in recent_trades:
            if amount > 500:
                cursor.execute("UPDATE market SET price = price + 30 WHERE stock = ?", (stock,))
            else:
                cursor.execute("UPDATE market SET price = price - 10 WHERE stock = ?", (stock,))

        # Incorporate faction influence
        cursor.execute("SELECT id, faction FROM players WHERE faction IS NOT NULL")
        faction_players = cursor.fetchall()
        for player_id, faction in faction_players:
            faction_system.manipulate_market(player_id, faction)  # ✅ Ensure function call matches faction_system

        conn.commit()