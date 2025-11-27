import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен вашего бота
BOT_TOKEN = "7809421116:AAEJ2D6BHkNzrCt1W2ZUW_bPFSiDYewaoN8"

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

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📚 *Доступные команды:*

/start - Начать работу
/help - Помощь и команды
/message - Помощь и команды
/info - Информация о боте
/markdown - Пример Markdown оформления
/buttons - Пример кнопок

*Реакции на слова:*
- Привет
- Пока
- Файл
- Картинка

*Также бот может:*
- Отправлять файлы
- Использовать Markdown
- Отвечать на сообщения
    """
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

# Команда /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = """
🤖 *Информация о боте*

*Версия:* 1.0
*Функции:*
• Ответы на команды
• Реакция на ключевые слова
• Поддржание общения
• Отправка файлов
• Инлайн кнопки

*Разработчик:* @SanitySpook
    """
    
    await update.message.reply_text(info_text, parse_mode='Markdown')

# Команда /markdown
async def markdown_example(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markdown_text = """
🎨 *Пример Markdown оформления*

*Жирный текст*
_Курсивный текст_
`Моноширинный текст`
[Ссылка](https://telegram.org)

*Список:*
- Пункт 1
- Пункт 2
- Пункт 3

*Нумерованный список:*
1. Первый
2. Второй
3. Третий

```python
# Пример кода
def hello():
    print("Hello World!")
```
    """
    
    await update.message.reply_text(markdown_text, parse_mode='Markdown')

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
        await query.edit_message_text("""
📚 *Помощь по боту*

*Команды:*
/start - Начать работу
/help - Помощь
/info - Информация
/invite - пригласить 
/dm - писать в лс
/user - информация о пользователе
/markdown - Markdown пример
/buttons - Кнопки
        """, parse_mode='Markdown')
    elif query.data == "info":
        await query.edit_message_text("""
🤖 *Информация*

Простой бот с функциями:
• Команды
• Реакции на слова
• Markdown
• Файлы
        """, parse_mode='Markdown')
    elif query.data == "back":
        await query.edit_message_text("🔙 Возврат в главное меню")

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if 'привет' in text:
        await update.message.reply_text(
            "👋 *Привет!* Рад тебя видеть!\n\n"
            "Как дела?",
            parse_mode='Markdown'
        )
    
    elif 'пока' in text:
        await update.message.reply_text(
            "👋 *До свидания!*\n\n"
            "Жду твоего возвращения!",
            parse_mode='Markdown'
        )
    
    elif 'файл' in text:
        # Создаем временный файл если его нет
        user = update.message.from_user
        text = update.message.text.lower()
        
        # Различные варианты имени пользователя
        first_name = user.first_name or ""
        last_name = user.last_name or ""
        full_name = f"{first_name} {last_name}".strip()
        username = f"@{user.username}" if user.username else "пользователь"
        with open('example.txt', 'w', encoding='utf-8') as f:
            f.write("Это пример текстового файла\nСоздан Telegram ботом!\n\n")
            f.write("Содержание файла:\n")
            f.write(" <Здесь пока ничего нет!>\n")
            f.write("Подпись:\n")
            f.write(f"{full_name} ({username})\n")
         
        # Отправка текстового файла
        with open('example.txt', 'rb') as file:
            await update.message.reply_document(
                document=file,
                filename="example.txt",
                caption="📄 *Вот текстовый файл*\n\nСоздан специально для демонстрации!",
                parse_mode='Markdown'
            )
    
    elif 'картинка' in text:
        # Отправка картинки по URL
        await update.message.reply_photo(
            photo='https://static.tildacdn.com/tild6237-6265-4232-a233-663832313834/noroot.png',
            caption="🖼️ *Пример картинки*\n\nВот так бот отправляет изображения!",
            parse_mode='Markdown'
        )
    
    else:
        await update.message.reply_text(
            f"🤔 *Я получил твое сообщение:*\n\n`{update.message.text}`\n\n"
            "Попробуй команду /help чтобы узнать что я умею!",
            parse_mode='Markdown'
        )


async def get_user_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Укажите username: /user @username")
        return
    
    username = context.args[0].replace('@', '')  # Убираем @ если есть
    
    try:
        # Пытаемся получить информацию о пользователе
        user = await context.bot.get_chat(f"@{username}")
        
        user_info = f"""
👤 *Информация о пользователе:*

*Username:* @{username}
*ID:* `{user.id}`
*Имя:* {user.first_name or 'Не указано'}
*Фамилия:* {user.last_name or 'Не указано'}
*Полное имя:* {user.full_name or 'Не указано'}
        """
        
        await update.message.reply_text(user_info, parse_mode='Markdown')
        
    except Exception as e:
        await update.message.reply_text(f"❌ Не удалось найти пользователя @{username}")

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

def escape_markdown(text: str, version: int = 1) -> str:
    """
    Экранирует специальные символы для Markdown
    version: 1 - Markdown, 2 - MarkdownV2
    """
    if version == 1:
        # Экранирование для Markdown
        escape_chars = r'\*_`\['
    else:
        # Экранирование для MarkdownV2 (более строгое)
        escape_chars = r'\_*[]()~`>#+-=|{}.!'
    
    for char in escape_chars:
        text = text.replace(char, f'\\{char}')
    return text

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


# Обработка документов
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    await update.message.reply_text(
        f"📎 *Получен файл!*\n\n"
        f"*Имя:* `{document.file_name}`\n"
        f"*MIME тип:* `{document.mime_type}`\n"
        f"*Размер:* `{document.file_size} байт`",
        parse_mode='Markdown'
    )

# Обработка фото
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖼️ *Классное фото!*\n\nСпасибо за изображение!",
        parse_mode='Markdown'
    )

# Обработка ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Ошибка: {context.error}")

# Основная функция
def main():
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("markdown", markdown_example))
    application.add_handler(CommandHandler("user", get_user_info))
    application.add_handler(CommandHandler("invite", invite_user_message))
    application.add_handler(CommandHandler("dm", send_direct_message))
    
    application.add_handler(CommandHandler("buttons", buttons))
    
    # Обработчики кнопок
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Обработчики сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    # Обработчик ошибок
    application.add_error_handler(error_handler)
    
    # Запускаем бота
    print("Бот запущен! Для остановки нажмите Ctrl+C")
    application.run_polling()

if __name__ == '__main__':
    main()




