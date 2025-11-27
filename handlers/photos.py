# Обработка фото
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖼️ *Классное фото!*\n\nСпасибо за изображение!",
        parse_mode='Markdown'
    )