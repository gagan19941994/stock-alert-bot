import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

async def send_alert(title, url, stock):
    status = "✅ IN STOCK" if stock else "❌ OUT OF STOCK"

    message = f"""
🚨 STOCK ALERT

📦 {title}

{status}

🔗 {url}
"""

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )
