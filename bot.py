from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

TOKEN = "8017242797:AAE4pGGObZ8KJnUdyne3sdZ6MVh_aLm5OII"

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Mini App Başlat", web_app=WebAppInfo(url="https://riseai-theta.vercel.app/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Mini App'ı başlatmak için tıklayın:", reply_markup=reply_markup)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
