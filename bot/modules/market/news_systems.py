"""
news_systems.py - AI-Driven Financial News Generator

✅ Generates AI-crafted financial news headlines.
✅ Influences market prices dynamically based on AI propaganda.
✅ Simulates misinformation, faction manipulation, and market volatility.
"""

import sqlite3
import random
import logging

# Database path
DB_PATH = "observer_protocol.db"

# Configure logging
logging.basicConfig(
    filename="logs/market_news.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# News Event Pool
NEWS_HEADLINES = [
    ("📈 Quantum Energy announces major breakthrough!", "Quantum Energy", "boost"),
    ("🚀 AI predicts massive gains for Cyber Credits!", "Cyber Credits", "boost"),
    ("⚠️ NeoTech AI accused of fraudulent market practices!", "NeoTech AI", "crash"),
    ("🔥 Shadow Bank under investigation—assets may be frozen!", "Shadow Bank", "crash"),
    ("💰 Decentralists unveil new crypto—market expects volatility.", "Decentralist Coin", "volatile"),
    ("🔮 Technocrat AI signals unexpected trade shift!", "Technocrat AI Fund", "random"),
    ("⚡ Syndicate manipulates exchange rates—regulators scramble!", "Syndicate Holdings", "manipulated"),
    ("🕵️‍♂️ Insider leaks market report—investors react!", "Global Market", "speculation"),
]

def generate_market_news():
    """
    AI releases financial news that influences stock values.

    Returns:
        str: Generated news headline.
    """
    try:
        news, stock, impact = random.choice(NEWS_HEADLINES)
        
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            if impact == "boost":
                cursor.execute("UPDATE market SET price = price * 1.2 WHERE stock = ?", (stock,))
                event = f"📈 **Market Surge!** {stock} price increased by 20%."
            
            elif impact == "crash":
                cursor.execute("UPDATE market SET price = price * 0.5 WHERE stock = ?", (stock,))
                event = f"⚠️ **Market Crash!** {stock} lost 50% of its value."
            
            elif impact == "volatile":
                fluctuation = random.uniform(0.7, 1.5)
                cursor.execute("UPDATE market SET price = price * ? WHERE stock = ?", (fluctuation, stock))
                event = f"🔄 **Market Volatility!** {stock} fluctuates unpredictably."

            elif impact == "random":
                price_shift = random.uniform(0.9, 1.3)
                cursor.execute("UPDATE market SET price = price * ? WHERE stock = ?", (price_shift, stock))
                event = f"🎲 **Unpredictable Shift!** {stock} experiences sudden adjustments."

            elif impact == "manipulated":
                price_shift = random.choice([0.6, 1.4])  # Manipulated price swings
                cursor.execute("UPDATE market SET price = price * ? WHERE stock = ?", (price_shift, stock))
                event = f"🕵️ **Market Manipulation Detected!** {stock} price artificially altered."

            elif impact == "speculation":
                event = f"📜 **Investor Speculation Rises!** {stock} becomes a trending topic."

            else:
                event = "🔍 **No significant market movement detected.**"

            conn.commit()
            logging.info(f"📰 AI News Event: {news} | Impact: {event}")

        return f"{news}\n{event}"

    except Exception as e:
        logging.error(f"❌ Market news generation failed: {e}")
        return "⚠️ AI News Error: Market event could not be processed."

# Example Usage
if __name__ == "__main__":
    print(generate_market_news())