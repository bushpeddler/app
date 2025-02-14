# news_system.py - Generates AI-driven financial news and misinformation

import sqlite3
import random

NEWS_HEADLINES = [
    ("📈 Quantum Energy announces major breakthrough!", "boost"),
    ("🚀 AI predicts massive gains for Cyber Credits!", "boost"),
    ("⚠️ NeoTech AI accused of fraudulent market practices!", "crash"),
    ("🔥 Shadow Bank under investigation—assets may be frozen!", "crash"),
    ("💰 Decentralists unveil new crypto—market expects volatility.", "volatile"),
]

def generate_market_news():
    """AI releases financial news that influences the market."""
    conn = sqlite3.connect("observer_protocol.db")
    cursor = conn.cursor()

    news, impact = random.choice(NEWS_HEADLINES)
    
    if impact == "boost":
        cursor.execute("UPDATE market SET price = price * 1.2 WHERE stock = 'Quantum Energy'")
    elif impact == "crash":
        cursor.execute("UPDATE market SET price = price * 0.5 WHERE stock = 'NeoTech AI'")
    elif impact == "volatile":
        cursor.execute("UPDATE market SET price = price * ?", (random.uniform(0.7, 1.5),))
    
    conn.commit()
    conn.close()
    
    return news