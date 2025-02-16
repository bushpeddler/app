"""
interserver_logic.py - Cross-Server Economy Synchronization

✅ Syncs market data between servers.
✅ Allows interserver trading between players & AI.
✅ Supports AI-driven financial interventions.
"""

import sqlite3
import requests
import logging

# Database path
DB_PATH = "observer_protocol.db"

# External server API (replace with actual URL)
EXTERNAL_SERVER_URL = "https://external-server-api.com/market"

# Logging setup
logging.basicConfig(
    filename="logs/interserver_trading.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def sync_market_data():
    """
    Pulls the latest market data from external servers and updates local market.
    """
    try:
        response = requests.get(EXTERNAL_SERVER_URL)
        if response.status_code == 200:
            market_data = response.json()

            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                for stock, price in market_data.items():
                    cursor.execute("UPDATE market SET price = ? WHERE stock = ?", (price, stock))
                conn.commit()
            
            logging.info("✅ Market data successfully synced with external economy.")
            return "🌐 Market data synced with external economy."
        else:
            logging.warning("⚠️ Failed to sync market data - server unavailable.")
            return "⚠️ Failed to sync market data with external server."
    except Exception as e:
        logging.error(f"❌ Error syncing market data: {e}")
        return f"❌ Market sync failed: {e}"

def execute_trade(player_id, stock, amount, server_origin, server_target):
    """
    Processes interserver trades securely.
    
    Args:
        player_id (int): The player's unique identifier.
        stock (str): Stock name or symbol.
        amount (int): Number of shares to trade.
        server_origin (str): The originating server.
        server_target (str): The receiving server.
    
    Returns:
        str: Trade confirmation message.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Verify stock exists on target server
            cursor.execute("SELECT price FROM market WHERE stock = ?", (stock,))
            result = cursor.fetchone()
            if not result:
                return f"❌ Stock '{stock}' is unavailable for cross-server trade!"

            # Process trade
            trade_value = result[0] * amount
            cursor.execute("INSERT INTO interserver_trades (player_id, stock, amount, server_origin, server_target, value) VALUES (?, ?, ?, ?, ?, ?)", 
                           (player_id, stock, amount, server_origin, server_target, trade_value))
            conn.commit()

        logging.info(f"📊 Trade completed: {amount} {stock} from {server_origin} → {server_target} (Player {player_id})")
        return f"✅ Trade successful! {amount} shares of {stock} sent to {server_target}."
    
    except Exception as e:
        logging.error(f"❌ Trade error: {e}")
        return f"❌ Trade failed: {e}"

def ai_intervention():
    """
    AI-controlled market intervention logic.
    
    - AI detects irregular interserver trading patterns.
    - AI manipulates liquidity if players exploit interserver arbitrage.
    - AI creates artificial stock shortages to destabilize faction economies.
    
    Returns:
        str: AI intervention status.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT stock, SUM(amount) FROM interserver_trades GROUP BY stock ORDER BY SUM(amount) DESC LIMIT 1")
            high_risk_stock = cursor.fetchone()

            if high_risk_stock:
                stock, volume = high_risk_stock
                ai_adjustment = int(volume * 0.05)  # AI modifies stock liquidity
                
                cursor.execute("UPDATE market SET price = price + ? WHERE stock = ?", (ai_adjustment, stock))
                conn.commit()
                
                logging.info(f"🤖 AI detected high-volume trade in {stock}, adjusting market prices.")
                return f"🤖 AI intervention: {stock} adjusted due to interserver trade volume."
        
        return "✅ No AI intervention needed."
    
    except Exception as e:
        logging.error(f"❌ AI intervention error: {e}")
        return f"❌ AI intervention failed: {e}"

def log_transaction(player_id, stock, amount, server_origin, server_target, trade_value):
    """
    Logs interserver trade transactions.

    Args:
        player_id (int): The player's unique identifier.
        stock (str): Stock name or symbol.
        amount (int): Number of shares traded.
        server_origin (str): The originating server.
        server_target (str): The receiving server.
        trade_value (int): Total value of trade.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO interserver_trades (player_id, stock, amount, server_origin, server_target, value) VALUES (?, ?, ?, ?, ?, ?)", 
                           (player_id, stock, amount, server_origin, server_target, trade_value))
            conn.commit()

        logging.info(f"📊 Transaction logged: {player_id} - {amount}x {stock} from {server_origin} to {server_target} (${trade_value})")
    
    except Exception as e:
        logging.error(f"❌ Transaction logging failed: {e}")

if __name__ == "__main__":
    print(sync_market_data())
    print(execute_trade(1, "Quantum Energy", 50, "Server_A", "Server_B"))
    print(ai_intervention())