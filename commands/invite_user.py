
async def invite_user_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Создает сообщение-приглашение для пользователя"""
    if not context.args:
        await update.message.reply_text(escape_markdown("❌ Укажите username: /invite @username"))
        return
    
    username = context.args[0].replace('@', '')
    
    invite_text = escape_markdown(f"""
*Приглашение для @{username}*

Чтобы бот мог вам писать, пожалуйста:
1. Напишите мне в ЛС: @{context.bot.username}
2. Или нажмите кнопку ниже

После этого бот сможет отправлять вам сообщения!
    """)
    
    keyboard = [
        [InlineKeyboardButton("Написать боту", url=escape_markdown(f"https://t.me/{context.bot.username}"))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        invite_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

