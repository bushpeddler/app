"""
ui.py - Consolidated Inline Button Definitions for Arcane Empires

This module provides inline keyboard functions for:
    - Main Menu (Trading, Hacking AI, Joining Factions)
    - Faction Selection
    - Trade Options (Faction-based strategies)
    - AI Morality Controls
    - Endgame Events
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# -----------------------------------------------
# 🎮 Main Menu (Primary User Actions)
# -----------------------------------------------

def main_menu():
    """
    Creates the main menu inline keyboard.
    
    Options include:
        - Trade
        - Hack AI
        - Join Faction
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📈 Trade", callback_data="trade"))
    keyboard.add(InlineKeyboardButton("🕵️ Hack AI", callback_data="hackAI"))
    keyboard.add(InlineKeyboardButton("⚔️ Join Faction", callback_data="joinFaction"))
    keyboard.add(InlineKeyboardButton("📊 Market Status", callback_data="marketStatus"))
    return keyboard

# -----------------------------------------------
# 🏴 Faction Selection Menu
# -----------------------------------------------

def faction_menu():
    """
    Creates the faction selection inline keyboard.
    
    Options include:
        - Syndicate
        - Technocrats
        - Decentralists
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔥 Join The Syndicate", callback_data="Syndicate"))
    keyboard.add(InlineKeyboardButton("🔵 Join The Technocrats", callback_data="Technocrats"))
    keyboard.add(InlineKeyboardButton("🟢 Join The Decentralists", callback_data="Decentralists"))
    return keyboard

# -----------------------------------------------
# 📈 Trading Menu (Faction-Based Strategies)
# -----------------------------------------------

def trade_menu():
    """
    Creates the inline keyboard for faction-based trading options.
    
    Options include:
        - Syndicate: Black Market Trade
        - Technocrats: AI-Optimized Investment
        - Decentralists: Crypto Speculation
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("💰 Syndicate: Black Market Trade", callback_data="syndicateTrade"))
    keyboard.add(InlineKeyboardButton("🤖 Technocrats: AI-Optimized Investment", callback_data="technocratTrade"))
    keyboard.add(InlineKeyboardButton("📈 Decentralists: Crypto Speculation", callback_data="decentralistTrade"))
    keyboard.add(InlineKeyboardButton("🔄 Return to Main Menu", callback_data="mainMenu"))
    return keyboard

# -----------------------------------------------
# 🤖 AI Morality Controls
# -----------------------------------------------

def ai_morality_menu():
    """
    Creates the inline keyboard for AI morality controls.
    
    Options include:
        - Check AI Morality
        - Trigger AI Trading Decision
        - Set AI Morality (Admin)
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🤖 Check AI Morality", callback_data="aiMorality"))
    keyboard.add(InlineKeyboardButton("📊 Trigger AI Trading Decision", callback_data="aiTradeDecision"))
    keyboard.add(InlineKeyboardButton("⚠️ Set AI Morality (Admin)", callback_data="setAIMorality"))
    keyboard.add(InlineKeyboardButton("🔄 Return to Main Menu", callback_data="mainMenu"))
    return keyboard

# -----------------------------------------------
# 🏛 Endgame Events Menu
# -----------------------------------------------

def endgame_menu():
    """
    Creates the inline keyboard for endgame event controls.
    
    Options include:
        - Trigger Market Collapse
        - Force AI Shutdown
        - Check Endgame Status
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("⚠️ Trigger Market Collapse", callback_data="triggerEvent"))
    keyboard.add(InlineKeyboardButton("🤖 Force AI Shutdown", callback_data="aiShutdown"))
    keyboard.add(InlineKeyboardButton("🏛 Check Endgame Status", callback_data="endgameStatus"))
    keyboard.add(InlineKeyboardButton("🔄 Return to Main Menu", callback_data="mainMenu"))
    return keyboard

# -----------------------------------------------
# 📊 Market Status & Trends Menu
# -----------------------------------------------

def market_overview_menu():
    """
    Creates the inline keyboard for market status and trends.
    
    Options include:
        - View Stock Prices
        - AI Market Predictions
        - Trade Options
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📉 View Stock Prices", callback_data="marketStatus"))
    keyboard.add(InlineKeyboardButton("🤖 AI Market Predictions", callback_data="ai_forecast"))
    keyboard.add(InlineKeyboardButton("📈 Trade Options", callback_data="trade"))
    keyboard.add(InlineKeyboardButton("🔄 Return to Main Menu", callback_data="mainMenu"))
    return keyboard