import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
#from config import *


from data import *


def escape_markdown(text: str, version: int = 1) -> str:
    if version == 1:
        escape_chars = r'\*_`\['
    else:
        escape_chars = r'\_*[]()~`>#+-=|{}.!'
    
    for char in escape_chars:
        text = text.replace(char, f'\\{char}')
    return text


def add_info_to_str(text, insert):
    for k, v in insert.items():
        text = text.replace(k,  escape_markdown(v))
    print(text)
async def debug_print(update: Update):
    user = update.message.from_user.username
    text = update.message.text.lower()
    print(f"Command from user {user}")
    return text
    


# Обработка ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Ошибка: {context.error}")
    print(f"Find command in message \n\'{text}\'")
















