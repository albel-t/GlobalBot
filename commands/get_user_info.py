async def get_user_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Укажите username: /user @username")
        return
    
    username = context.args[0].replace('@', '')  # Убираем @ если есть
    
    try:
        # Пытаемся получить информацию о пользователе
        user = await context.bot.get_chat(f"@{username}")
        
        user_info = f"""
👤 *Информация о пользователе:*

*Username:* @{username}
*ID:* `{user.id}`
*Имя:* {user.first_name or 'Не указано'}
*Фамилия:* {user.last_name or 'Не указано'}
*Полное имя:* {user.full_name or 'Не указано'}
        """
        
        await update.message.reply_text(user_info, parse_mode='Markdown')
        
    except Exception as e:
        await update.message.reply_text(f"❌ Не удалось найти пользователя @{username}")
