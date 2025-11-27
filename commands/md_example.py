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

