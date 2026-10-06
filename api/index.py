import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are the tasks you can perform:\n/start - Start the conversatin")

async def send_startup_msg(application):
    try:
        chat_id = "6532541099"
        await application.bot.send_message(
            chat_id=chat_id, 
            text="✅ Welcome to Echo! Use /start to begin a productive conversation with me."
        )
    except Exception as e:
        logger.warning(f"Could not send startup message: {e}")

if __name__ == "__main__":
    BOT_TOKEN = "8776721705:AAGoVNrU3IM4xxtFYjy22k_FA1ofjmhl0eY"

    # Using parentheses instead of backslashes for safer line breaks
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(send_startup_msg)
        .build()
    )

    app.add_handler(CommandHandler("start", start))

    print("Bot is running and listening for updates...")
    app.run_polling()
