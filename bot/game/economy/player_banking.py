# player_banking.py - Players create banks, hedge funds, and investment firms

import sqlite3

def create_bank(player_id, bank_name):
    """Players establish financial institutions."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO banks (owner, name, capital) VALUES (?, ?, 5000)", (player_id, bank_name))
    conn.commit()
    conn.close()
    return f"🏦 {bank_name} has been established with 5000 credits in starting capital."

def deposit_money(player_id, bank_name, amount):
    """Players deposit funds into a bank."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE players SET wealth = wealth - ? WHERE id = ?", (amount, player_id))
    cursor.execute("UPDATE banks SET capital = capital + ? WHERE name = ?", (amount, bank_name))

    conn.commit()
    conn.close()
    return f"💰 {amount} credits deposited into {bank_name}."