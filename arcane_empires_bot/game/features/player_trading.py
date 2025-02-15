# player_trading.py - Enables direct player trading & price manipulation

import sqlite3

def player_trade(sender_id, receiver_id, stock, amount):
    """Allows players to trade directly."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    # Check sender’s balance
    cursor.execute("SELECT wealth FROM players WHERE id = ?", (sender_id,))
    sender_wealth = cursor.fetchone()[0]

    # Check current stock price
    cursor.execute("SELECT price FROM market WHERE stock = ?", (stock,))
    stock_price = cursor.fetchone()[0]

    total_cost = stock_price * amount

    if sender_wealth < total_cost:
        conn.close()
        return "❌ Not enough credits to complete trade."

    # Deduct from sender, add to receiver
    cursor.execute("UPDATE players SET wealth = wealth - ? WHERE id = ?", (total_cost, sender_id))
    cursor.execute("UPDATE players SET wealth = wealth + ? WHERE id = ?", (total_cost, receiver_id))

    conn.commit()
    conn.close()
    return f"✅ Trade complete! {receiver_id} received {amount} shares of {stock}."