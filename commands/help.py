# Команда /help
from config import *

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await debug_print(update)
    help_text = text["help-command"]
    
    await update.message.reply_text(help_text, parse_mode='Markdown')
