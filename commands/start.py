# Команда /start
from config import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    keyboard = [
        [InlineKeyboardButton("Помощь", callback_data="help")],
        [InlineKeyboardButton("Информация", callback_data="info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(text['start-command'],
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )




