from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

# Bot token you get from BotFather
TOKEN = "8017242797:AAE4pGGObZ8KJnUdyne3sdZ6MVh_aLm5OII"

# /start command function
async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Mini App Başlat", web_app=WebAppInfo(url="https://riseai-theta.vercel.app/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Mini App'ı başlatmak için tıklayın:", reply_markup=reply_markup)

# Main function to run the bot
def main():
    # Create the application using the bot token
    application = Application.builder().token(TOKEN).build()

    # Add handler for the /start command
    application.add_handler(CommandHandler("start", start))

    # Run the bot with async methods
    application.run_polling()

if __name__ == '__main__':
    main()