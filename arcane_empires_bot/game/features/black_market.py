# black_market.py - Underground economy that avoids AI regulation

import sqlite3
import random

BLACK_MARKET_ASSETS = {
    "Illegal Crypto": 500,
    "Data Exploits": 1200,
    "Confidential Trading Reports": 2500,
}

def access_black_market(player_id):
    """Allows players to trade in an AI-free market."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    asset = random.choice(list(BLACK_MARKET_ASSETS.keys()))
    price = BLACK_MARKET_ASSETS[asset]

    # Deduct player balance
    cursor.execute("UPDATE players SET wealth = wealth - ? WHERE id = ?", (price, player_id))

    conn.commit()
    conn.close()

    return f"⚠️ You purchased **{asset}** for {price} credits. AI is not aware of this trade."