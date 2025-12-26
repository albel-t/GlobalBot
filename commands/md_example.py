# Команда /markdown
from config import *

async def markdown_example(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markdown_text = text['example-md']
    
    await update.message.reply_text(markdown_text, parse_mode='Markdown')

