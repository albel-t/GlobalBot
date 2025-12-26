from config import *


async def invite_user_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Создает сообщение-приглашение для пользователя"""
    if not context.args:
        await update.message.reply_text(escape_markdown(text['invite-wrong-enter']))
        return
    print(context.args[0])
    username = context.args[0].replace('@', '')
    
    
    invite_text = add_info_to_str(text['invite'], {'username': username})
    
    
    keyboard = [
        [InlineKeyboardButton("Написать боту", url=escape_markdown(f"https://t.me/{context.bot.username}"))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    print(invite_text)
    await update.message.reply_text(
        text=invite_text,
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

