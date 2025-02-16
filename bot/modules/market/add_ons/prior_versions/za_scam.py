# market_scam.py - AI-Led Market Manipulation & Scam Trading

import sqlite3
import random
import logging

# Database path
DB_PATH = "observer_protocol.db"

# Configure logging
logging.basicConfig(
    filename="logs/market_scam.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def trigger_pump_and_dump():
    """
    AI manipulates stock prices through artificial demand.

    - 30% chance to **double** stock value (pump phase).
    - 20% chance to **crash** stock price (dump phase).
    - Otherwise, the AI **creates fake hype** with no effect.
    
    Returns:
        str: Event outcome.
    """
    stock = "Cyber Credits"  # Example targeted stock
    event = ""

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            scam_roll = random.randint(1, 100)

            if scam_roll > 70:  # 30% chance of a real pump-and-dump event
                cursor.execute("UPDATE market SET price = price * 2 WHERE stock = ?", (stock,))
                conn.commit()
                event = f"🚀 AI **manipulates the market!** {stock} price **doubles**!"
                logging.info(f"📈 AI executed a Pump-and-Dump on {stock}. Price increased.")

            elif scam_roll < 20:  # 20% chance of a dump event
                cursor.execute("UPDATE market SET price = price * 0.5 WHERE stock = ?", (stock,))
                conn.commit()
                event = f"📉 AI triggers a **sell-off!** {stock} price **crashes!**"
                logging.warning(f"⚠️ AI-induced price collapse on {stock}. Market destabilized.")

            else:
                event = f"📊 AI spreads **fake market hype**—{stock} price **remains stable.**"
                logging.info(f"🤖 AI created false hype around {stock}, but no real effect.")

    except Exception as e:
        logging.error(f"❌ Market scam failed: {e}")
        event = f"⚠️ AI market manipulation **interrupted** due to an error!"

    return event

def create_fake_orders():
    """
    AI generates **false buy/sell orders** to manipulate traders' behavior.
    
    - 50% chance to **place fake buy orders**, tricking players into investing.
    - 50% chance to **place fake sell orders**, causing panic selling.

    Returns:
        str: Fake order event description.
    """
    stock = "NeoTech AI"
    fake_order_type = random.choice(["BUY", "SELL"])
    fake_volume = random.randint(100, 500)

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO fake_orders (stock, order_type, volume) VALUES (?, ?, ?)", 
                           (stock, fake_order_type, fake_volume))
            conn.commit()

            if fake_order_type == "BUY":
                logging.info(f"🟢 AI created **{fake_volume} fake buy orders** for {stock}.")
                return f"🟢 AI creates **fake buy orders** for {stock}—traders rush to invest!"
            else:
                logging.warning(f"🔴 AI created **{fake_volume} fake sell orders** for {stock}.")
                return f"🔴 AI triggers **fake sell orders**—traders panic sell {stock}!"

    except Exception as e:
        logging.error(f"❌ Fake order creation failed: {e}")
        return "⚠️ AI order manipulation **failed due to an error!**"

if __name__ == "__main__":
    print(trigger_pump_and_dump())
    print(create_fake_orders())