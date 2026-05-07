import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

import database
from scraper import fetch_ongoing_exams

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize DB
database.init_db()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command. Adds user to subscribers."""
    chat_id = update.effective_chat.id
    username = update.effective_user.username
    logger.info(f"Received /start command from user: {username} (ID: {chat_id})")
    
    if database.add_subscriber(chat_id):
        logger.info(f"New subscriber added: {chat_id}")
        await context.bot.send_message(
            chat_id=chat_id,
            text="Welcome to the SL Government Exam Tracker! 🎓\n\nYou are now subscribed. You will receive a notification here whenever a new exam is posted on applications.doenets.lk.\n\nTo unsubscribe, use /stop."
        )
    else:
        logger.info(f"User {chat_id} already exists in subscribers.")
        await context.bot.send_message(
            chat_id=chat_id,
            text="You are already subscribed to notifications! 🔔\n\nUse /stop to unsubscribe."
        )

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /stop command. Removes user from subscribers."""
    chat_id = update.effective_chat.id
    logger.info(f"Received /stop command from user: {chat_id}")
    database.remove_subscriber(chat_id)
    await context.bot.send_message(
        chat_id=chat_id,
        text="You have been unsubscribed from notifications. 🔕\n\nUse /start to subscribe again."
    )

async def check_exams_job(context: ContextTypes.DEFAULT_TYPE):
    """The job that runs periodically to check for new exams."""
    logger.info("Running scheduled exam check...")
    exams = fetch_ongoing_exams()
    
    if not exams:
        logger.info("No exams found or error fetching.")
        return

    new_exams = []
    for exam in exams:
        exam_id = str(exam.get('id', ''))
        name = exam.get('name', 'Unknown Exam')
        
        if exam_id and database.is_exam_new(exam_id, name):
            new_exams.append(exam)
            
    if new_exams:
        logger.info(f"Found {len(new_exams)} new exams. Notifying subscribers...")
        subscribers = database.get_subscribers()
        
        for exam in new_exams:
            msg = (
                f"🚨 *NEW EXAM POSTED* 🚨\n\n"
                f"📚 *{exam.get('name')}*\n\n"
                f"💰 Fee: {exam.get('price')} LKR\n"
                f"📅 Starts: {exam.get('start_date')}\n"
                f"⏳ Ends: {exam.get('end_date')}\n\n"
                f"🔗 [Apply Here](https://applications.doenets.lk/exams)"
            )
            
            for chat_id in subscribers:
                try:
                    await context.bot.send_message(
                        chat_id=chat_id,
                        text=msg,
                        parse_mode='Markdown',
                        disable_web_page_preview=True
                    )
                except Exception as e:
                    logger.error(f"Failed to send message to {chat_id}: {e}")
    else:
        logger.info("No new exams found.")

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set.")
        return

    application = ApplicationBuilder().token(token).build()

    # Commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('stop', stop))

    # Job Queue (Runs daily. Interval is in seconds)
    # 86400 seconds = 1 day
    # Or we can specify a time of day
    interval = int(os.getenv("POLL_INTERVAL", 86400)) 
    
    # We run it once immediately (with small delay) to check, then daily
    application.job_queue.run_repeating(check_exams_job, interval=interval, first=10)

    # Start polling
    logger.info("Starting bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
