import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from commands import *
from handlers import *
from config import *
# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен вашего бота
BOT_TOKEN = "7809421116:AAEJ2D6BHkNzrCt1W2ZUW_bPFSiDYewaoN8"



# Основная функция
def main():
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info_command))
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




