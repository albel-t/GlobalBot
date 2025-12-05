
from config import *

async def send_direct_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправка сообщения пользователю в ЛС по username"""
    if len(context.args) < 2:
        await update.message.reply_text("❌ Формат: /dm @username Текст сообщения")
        return
    
    username = context.args[0].replace('@', '')
    message_text = " ".join(context.args[1:])
    
    try:
        # Получаем chat_id пользователя
        user_chat = await context.bot.get_chat(f"@{username}")
        
        # Отправляем сообщение
        await context.bot.send_message(
            chat_id=user_chat.id,
            text=f"📨 *Сообщение от бота:*\n\n{message_text}",
            parse_mode='Markdown'
        )
        
        await update.message.reply_text(f"✅ Сообщение отправлено пользователю @{username}")
        
    except Exception as e:
        await update.message.reply_text(f"❌ Ошибка отправки: {e}")
