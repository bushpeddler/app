# player_banking.py - Player-Run Financial Institutions

import sqlite3
import logging

# Database path
DB_PATH = "observer_protocol.db"

# Configure logging
logging.basicConfig(
    filename="logs/player_banking.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def create_bank(player_id, bank_name):
    """
    Allows players to establish financial institutions.

    Args:
        player_id (int): The ID of the player founding the bank.
        bank_name (str): The name of the bank.

    Returns:
        str: Confirmation message.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Check if bank already exists
            cursor.execute("SELECT name FROM banks WHERE name = ?", (bank_name,))
            if cursor.fetchone():
                return f"⚠️ Bank '{bank_name}' already exists!"

            # Create new bank with starting capital
            cursor.execute("INSERT INTO banks (owner, name, capital) VALUES (?, ?, ?)", (player_id, bank_name, 5000))
            conn.commit()

            logging.info(f"🏦 Bank Created: {bank_name} by Player {player_id}")
            return f"🏦 {bank_name} has been established with 5000 credits in starting capital."

    except Exception as e:
        logging.error(f"❌ Error creating bank: {e}")
        return f"❌ Bank creation failed: {e}"

def deposit_money(player_id, bank_name, amount):
    """
    Allows players to deposit funds into a player-run bank.

    Args:
        player_id (int): The ID of the depositing player.
        bank_name (str): The name of the bank.
        amount (int): The deposit amount.

    Returns:
        str: Confirmation message.
    """
    if amount <= 0:
        return "⚠️ Deposit amount must be greater than zero."

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Verify player has enough wealth
            cursor.execute("SELECT wealth FROM players WHERE id = ?", (player_id,))
            player_wealth = cursor.fetchone()
            if not player_wealth or player_wealth[0] < amount:
                return "❌ Insufficient funds!"

            # Verify bank exists
            cursor.execute("SELECT capital FROM banks WHERE name = ?", (bank_name,))
            bank = cursor.fetchone()
            if not bank:
                return f"❌ Bank '{bank_name}' does not exist!"

            # Transfer funds
            cursor.execute("UPDATE players SET wealth = wealth - ? WHERE id = ?", (amount, player_id))
            cursor.execute("UPDATE banks SET capital = capital + ? WHERE name = ?", (amount, bank_name))
            conn.commit()

            logging.info(f"💰 Player {player_id} deposited {amount} credits into {bank_name}.")
            return f"💰 {amount} credits deposited into {bank_name}."

    except Exception as e:
        logging.error(f"❌ Error processing deposit: {e}")
        return f"❌ Deposit failed: {e}"

def withdraw_money(player_id, bank_name, amount):
    """
    Allows players to withdraw funds from their bank.

    Args:
        player_id (int): The ID of the withdrawing player.
        bank_name (str): The name of the bank.
        amount (int): The withdrawal amount.

    Returns:
        str: Confirmation message.
    """
    if amount <= 0:
        return "⚠️ Withdrawal amount must be greater than zero."

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Verify bank exists and is owned by the player
            cursor.execute("SELECT capital, owner FROM banks WHERE name = ?", (bank_name,))
            bank = cursor.fetchone()
            if not bank:
                return f"❌ Bank '{bank_name}' does not exist!"
            if bank[1] != player_id:
                return "⚠️ You do not own this bank."

            # Verify bank has enough capital for withdrawal
            if bank[0] < amount:
                return "❌ Insufficient bank capital for withdrawal!"

            # Process withdrawal
            cursor.execute("UPDATE banks SET capital = capital - ? WHERE name = ?", (amount, bank_name))
            cursor.execute("UPDATE players SET wealth = wealth + ? WHERE id = ?", (amount, player_id))
            conn.commit()

            logging.info(f"💸 Player {player_id} withdrew {amount} credits from {bank_name}.")
            return f"💸 {amount} credits withdrawn from {bank_name}."

    except Exception as e:
        logging.error(f"❌ Error processing withdrawal: {e}")
        return f"❌ Withdrawal failed: {e}"

if __name__ == "__main__":
    # Example test cases (replace with real player IDs in use)
    print(create_bank(1, "NeoFinance"))
    print(deposit_money(1, "NeoFinance", 200))
    print(withdraw_money(1, "NeoFinance", 100))