"""
config.py - Bot Configuration Settings

This module centralizes:
✅ Telegram Bot Token
✅ Web Dashboard URL
✅ Database Filepath
✅ AI Trading & Market Configurations
"""

# 🔑 Telegram Bot Token
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# 🌍 Web Dashboard URL
WEB_DASHBOARD_URL = "http://127.0.0.1:5000/"  # Change this if deploying live

# 📊 Database Connection
DATABASE_FILE = "observer_protocol.db"

# 🔍 AI & Market Configurations
MARKET_REFRESH_RATE = 30  # Seconds before market updates
AI_TRADING_ACTIVE = True  # Enable AI-driven market behavior