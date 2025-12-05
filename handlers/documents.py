from config import *

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
