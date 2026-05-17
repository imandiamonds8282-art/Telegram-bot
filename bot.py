from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8723758287:AAHUy3a3jQ1r6xwmjJTe9SgYBikuzT7vfXU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 😄 ربات روشنه!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
