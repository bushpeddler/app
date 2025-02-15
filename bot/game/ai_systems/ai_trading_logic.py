"""
ai_trading_logic.py - AI Market Trading Decisions

This module adjusts market prices based on the AI's morality setting.
"""

import sqlite3
import ai_morality
import random

DEFAULT_MARKET_BEHAVIOR = lambda: random.randint(-2, 2)  # Default small fluctuations
MIN_PRICE, MAX_PRICE = 5, 5000  # Enforces price stability

def ai_trade_decision():
    """
    Adjusts market prices based on Observer AI morality.

    The function:
    - Retrieves AI morality state from 'global_state' table.
    - Uses the corresponding market behavior from ai_morality.py.
    - Applies price changes with upper/lower limits.

    Returns:
        str: Market adjustment report.
    """
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()

        # Retrieve AI morality
        cursor.execute("SELECT ai_morality FROM global_state")
        result = cursor.fetchone()
        ai_morality_state = result[0] if result else "Neutral"

        # Get AI behavior function, fallback to default if undefined
        market_behavior = ai_morality.AI_MORALITY_TYPES.get(ai_morality_state, {"market_behavior": DEFAULT_MARKET_BEHAVIOR})["market_behavior"]

        # Retrieve all stocks
        cursor.execute("SELECT stock FROM market")
        stocks = cursor.fetchall()

        # Apply AI-driven adjustments with limits
        for (stock_name,) in stocks:
            price_change = market_behavior()
            cursor.execute(
                "UPDATE market SET price = MIN(MAX(price + ?, ?, ?)) WHERE stock = ?",
                (price_change, MIN_PRICE, MAX_PRICE, stock_name)
            )

    return f"📊 Observer AI ({ai_morality_state}) adjusted market prices."