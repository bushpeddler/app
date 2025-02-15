"""
commands.py - Arcane Empires: Telegram Commands

This version includes:
✅ Market System Commands
✅ AI Trading & Morality Commands
✅ Faction-Based Economy Commands
✅ Endgame Mechanics
✅ Web Dashboard Integration
"""

from aiogram import types, Dispatcher
import config
from economy import market_engine  # ✅ Corrected import
import database
import event_system
import faction_system
import unlock_system
import ai_morality
import ai_trading_logic
import endgame_scenarios
import ui

dp = Dispatcher()

# -----------------------------------------------
# 📊 Market System Commands
# -----------------------------------------------

@dp.message_handler(commands=['market_status'])
async def market_status(message: types.Message):
    """Returns live stock market updates."""
    market_data = market_engine.get_market_status()
    status_message = "\n".join([f"{stock}: {price} credits" for stock, price in market_data.items()])
    await message.answer(f"📊 **Market Status:**\n{status_message}")

@dp.message_handler(commands=['ai_forecast'])
async def ai_forecast(message: types.Message):
    """Provides AI prediction for market trends."""
    prediction = event_system.trigger_event()
    await message.answer(f"🤖 **AI Market Forecast:**\n{prediction}")

@dp.message_handler(commands=['trade_history'])
async def trade_history(message: types.Message):
    """Returns the last 5 trades a player made."""
    history = database.get_trade_history(message.from_user.id)
    history_message = "\n".join([f"{trade[1]}: {trade[2]} credits" for trade in history])
    await message.answer(f"📜 **Trade History:**\n{history_message if history else 'No trades yet!'}")

# -----------------------------------------------
# 🏴 Faction-Based Economy Commands
# -----------------------------------------------

@dp.message_handler(commands=['faction_status'])
async def faction_status(message: types.Message):
    """Returns the player's faction influence."""
    effects = faction_system.get_faction_effects(message.from_user.id)
    await message.answer(f"⚡ **Faction Influence:** {effects['effect']}")

@dp.message_handler(commands=['market_manipulation'])
async def market_manipulation(message: types.Message):
    """Attempts to manipulate the market based on faction skills."""
    result = faction_system.manipulate_market(message.from_user.id)
    await message.answer(f"📊 **Market Manipulation:**\n{result}")

@dp.message_handler(commands=['trade_with_faction'])
async def trade_with_faction(message: types.Message):
    """Allows players to trade within their faction's economy."""
    await message.answer("📈 Choose a trade strategy:", reply_markup=ui.trade_menu())

# -----------------------------------------------
# 📈 Game Phase Commands
# -----------------------------------------------

@dp.message_handler(commands=['check_phase'])
async def check_phase(message: types.Message):
    """Returns the current unlock phase for the player."""
    phase = unlock_system.check_progress(message.from_user.id)
    await message.answer(f"📊 **Current Game Phase:** {phase}")

# -----------------------------------------------
# 🤖 AI Morality & Trading Commands
# -----------------------------------------------

@dp.message_handler(commands=['ai_morality_status'])
async def ai_morality_status(message: types.Message):
    """Displays AI's current ethical stance."""
    morality = ai_morality.get_current_morality()
    await message.answer(f"🤖 **Observer AI Morality:** {morality}")

@dp.message_handler(commands=['set_ai_morality'])
async def set_ai_morality(message: types.Message):
    """Admin command to manually adjust AI morality."""
    try:
        new_morality = message.text.split(" ", 1)[1]
    except IndexError:
        await message.answer("⚠️ Please provide a morality value. Usage: /set_ai_morality <value>")
        return
    
    result = ai_morality.set_ai_morality(new_morality)
    await message.answer(result)

@dp.message_handler(commands=['ai_trade_decision'])
async def ai_trade_decision(message: types.Message):
    """Triggers AI trading behavior based on its morality."""
    result = ai_trading_logic.ai_trade_decision()
    await message.answer(result)

# -----------------------------------------------
# 🏛 Endgame Mechanics Commands
# -----------------------------------------------

@dp.message_handler(commands=['endgame_status'])
async def endgame_status(message: types.Message):
    """Checks if an endgame condition has been met."""
    status = endgame_scenarios.check_endgame_status()
    await message.answer(f"🏛 **Endgame Status:**\n{status}")

@dp.message_handler(commands=['trigger_event'])
async def trigger_event(message: types.Message):
    """Manually triggers an economic event (for testing or admin use)."""
    event_result = event_system.trigger_event()
    await message.answer(f"📊 **Event Triggered:**\n{event_result}")

@dp.message_handler(commands=['ai_shutdown'])
async def ai_shutdown(message: types.Message):
    """Triggers AI collapse manually (for admin use)."""
    shutdown_result = endgame_scenarios.ai_shutdown()
    await message.answer(f"💥 **AI Shutdown Triggered:**\n{shutdown_result}")

# -----------------------------------------------
# 🌍 Web Dashboard Integration
# -----------------------------------------------

@dp.message_handler(commands=['dashboard'])
async def dashboard_link(message: types.Message):
    """Sends the link to the web dashboard."""
    await message.answer(
        f"🌍 **Arcane Empires Web Dashboard**\n[Click Here to View]({config.WEB_DASHBOARD_URL})",
        parse_mode="Markdown"
    )