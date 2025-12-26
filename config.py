import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
#from config import *


from data import *


def escape_markdown(input_text: str, version: int = 1) -> str:
    if version == 1:
        escape_chars = r'\*_`\['
    else:
        escape_chars = r'\_*[]()~`>#+-=|{}.!'
    
    for char in escape_chars:
        input_text = input_text.replace(char, f'\\{char}')
    return input_text


def add_info_to_str(input_text: str, insert):
    print(f"input data add_info_to_str(input_text: {type(input_text)}, insert: {type(insert)}) : ")
    print(f"input_text {input_text}")
    print(f"insert {insert}")
    for k, v in insert.items():
        input_text = input_text.replace(k,  escape_markdown(v))
    print(input_text)
    return input_text


async def debug_print(update: Update):
    user = update.message.from_user.username
    input_text = update.message.text.lower()
    print(f"Command from user {user}")
    return input_text
    


# Обработка ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_text = update.message.text.lower()
    logging.error(f"Ошибка: {context.error}")
    print(f"Find command in message \n\'{input_text}\'")
















