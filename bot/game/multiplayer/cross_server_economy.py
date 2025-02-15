# cross_server_economy.py - Global economy shared across multiple servers

import sqlite3
import requests

def sync_market_data():
    """Pulls the latest market data from other game servers."""
    external_server_url = "https://external-server-api.com/market"

    response = requests.get(external_server_url)
    if response.status_code == 200:
        market_data = response.json()
        
        conn = sqlite3.connect("observer_protocol.db")
        cursor = conn.cursor()
        
        for stock, price in market_data.items():
            cursor.execute("UPDATE market SET price = ? WHERE stock = ?", (price, stock))
        
        conn.commit()
        conn.close()
        return "🌐 Market data synced with external economy."
    else:
        return "⚠️ Failed to sync market data with external server."