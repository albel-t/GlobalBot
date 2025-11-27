# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Помощь", callback_data="help")],
        [InlineKeyboardButton("Информация", callback_data="info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 *Привет! Я связующий бот*\n\n"
        "Используй /help чтобы увидеть все команды",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )



