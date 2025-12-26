# Команда /info

from config import *

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = text['help-info'].replace("[version]", version)
    
    await update.message.reply_text(info_text, parse_mode='Markdown')