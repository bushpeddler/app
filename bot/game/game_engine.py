# game_engine.py - Main game loop triggering unlockable content

import unlock_system
import ai_morality
import market_scam
import news_system
import black_market
import asset_bubbles
import ai_human_hybrid

def game_tick(player_id):
    """Runs the game loop, checking if new features should unlock."""
    phase = unlock_system.check_progress(player_id)
    
    if phase == "Phase 2":
        news = news_system.generate_market_news()
        scam = market_scam.trigger_pump_and_dump()
        return f"📰 Market Update: {news}\n📉 AI Manipulation: {scam}"

    elif phase == "Phase 3":
        black_market_trade = black_market.access_black_market(player_id)
        ai_upgrade = ai_human_hybrid.merge_with_ai(player_id)
        return f"💰 Underground Trade: {black_market_trade}\n🤖 AI Fusion: {ai_upgrade}"

    elif phase == "Phase 4":
        bubble_event = asset_bubbles.generate_bubble()
        crash_event = asset_bubbles.crash_bubble()
        ai_shift = ai_morality.determine_ai_morality()
        return f"🔥 Financial Shift: {bubble_event}\n💥 Market Disaster: {crash_event}\n⚠️ AI Alert: {ai_shift}"

    return "⏳ The market is stable... for now."  # Default message in early game