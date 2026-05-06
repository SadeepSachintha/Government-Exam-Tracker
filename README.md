# 🎓 SL Government Exam Tracker Bot

A lightweight, automated Telegram Bot that monitors the [Department of Examinations Sri Lanka](https://applications.doenets.lk/exams) website and instantly notifies subscribers when new government exams are posted.

## ✨ Features
- **Real-time Notifications:** Get alerts directly on your phone as soon as an exam is published.
- **Easy Subscriptions:** Users can easily opt-in or opt-out by messaging `/start` and `/stop`.
- **Automated Polling:** Background jobs check for new exams periodically without manual intervention.
- **Smart Tracking:** Uses SQLite to remember which exams have already been broadcasted, preventing duplicate alerts.
- **Docker Ready:** Includes a `Dockerfile` and `docker-compose.yml` for zero-dependency deployment anywhere.

## 🚀 Local Development

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd G-exams
   ```

2. **Install dependencies:**
   Make sure you have Python 3.8+ installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your environment:**
   - Talk to [@BotFather](https://t.me/botfather) on Telegram to create a new bot and get your HTTP API Token.
   - Create a `.env` file in the project root:
     ```env
     TELEGRAM_BOT_TOKEN=your_bot_token_here
     POLL_INTERVAL=86400  # Interval in seconds (86400 = 24 hours)
     ```

4. **Run the bot:**
   ```bash
   python bot.py
   ```

## 🐳 Deployment (Docker / Ubuntu VM)

1. **Install Docker & Docker Compose** (if not already installed):
   ```bash
   sudo apt update
   sudo apt install docker.io docker-compose
   sudo systemctl enable --now docker
   ```

2. **Configure your `.env` file** as shown in the Local Development section.

3. **Deploy the container:**
   ```bash
   sudo docker-compose up -d
   ```

4. **View live logs:**
   ```bash
   sudo docker-compose logs -f
   ```

---
*Built with Python, python-telegram-bot, and Docker.*
