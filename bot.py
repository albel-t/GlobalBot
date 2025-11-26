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
        "👋 *Привет! Я простой бот*\n\n"
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
• Markdown оформление
• Отправка файлов
• Инлайн кнопки

*Разработчик:* Ты 😊
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
        if not os.path.exists('example.txt'):
            with open('example.txt', 'w', encoding='utf-8') as f:
                f.write("Это пример текстового файла\nСоздан Telegram ботом!\n\n")
                f.write("Содержание файла:\n")
                f.write("1. Первая строка\n")
                f.write("2. Вторая строка\n")
                f.write("3. Третья строка\n")
        
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
            photo='https://via.placeholder.com/400x200/0088cc/ffffff?text=Пример+картинки+от+бота',
            caption="🖼️ *Пример картинки*\n\nВот так бот отправляет изображения!",
            parse_mode='Markdown'
        )
    
    else:
        await update.message.reply_text(
            f"🤔 *Я получил твое сообщение:*\n\n`{update.message.text}`\n\n"
            "Попробуй команду /help чтобы узнать что я умею!",
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




