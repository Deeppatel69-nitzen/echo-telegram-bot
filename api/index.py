import logging
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are the tasks you can perform:\n/start - Start the conversation"
    )

async def send_startup_msg(application):
    try:
        chat_id = "6532541099"
        await application.bot.send_message(
            chat_id=chat_id,
            text="✅ Welcome to Echo! Use /start to begin a productive conversation with me."
        )
    except Exception as e:
        logger.warning(f"Could not send startup message: {e}")

BOT_TOKEN = "8776721705:AAGoVNrU3M4xxtFYjy22k_FA1ofjmhl0eY"

telegram_app = (
    ApplicationBuilder()
    .token(BOT_TOKEN)
    .post_init(send_startup_msg)
    .build()
)

telegram_app.add_handler(CommandHandler("start", start))

app = FastAPI()

@app.post("/api/index")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.initialize()
    await telegram_app.process_update(update)
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "Bot is running!"}
