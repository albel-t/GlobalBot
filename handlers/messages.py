from config import *


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
