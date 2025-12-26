
from config import *


# Команда /buttons
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Кнопка 1", callback_data="button1"),
            InlineKeyboardButton("Кнопка 2", callback_data="button2"),
        ],
        [
            InlineKeyboardButton("Ссылка", url="https://telegram.org"),
            InlineKeyboardButton("Назад", callback_data="back"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🔘 *Пример кнопок:*\n\nВыберите действие:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )



# Обработка нажатий на кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "button1":
        await query.edit_message_text("✅ Вы нажали *Кнопку 1*!", parse_mode='Markdown')
    elif query.data == "button2":
        await query.edit_message_text("✅ Вы нажали *Кнопку 2*!", parse_mode='Markdown')
    elif query.data == "help":
        await query.edit_message_text(text['help-command'], parse_mode='Markdown')
    elif query.data == "info":
        await query.edit_message_text(text['help-info'].replace("[version]", version), parse_mode='Markdown')
    elif query.data == "back":
        await query.edit_message_text("🔙 Возврат в главное меню")
