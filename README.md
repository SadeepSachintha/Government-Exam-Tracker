# 🎓 SL Government Exam Tracker Bot

A lightweight, automated Telegram Bot that monitors the [Department of Examinations Sri Lanka](https://applications.doenets.lk/exams) website and instantly notifies subscribers when new government exams are posted.

## ✨ Features
- **Real-time Notifications:** Get alerts directly on your phone as soon as an exam is published.
- **Easy Subscriptions:** Users can easily opt-in or opt-out by messaging `/start` and `/stop`.
- **Premium Web Dashboard:** A beautiful, dark-mode web interface to monitor subscribers, tracked exams, and bot health in real-time.
- **Automated Polling:** Background jobs check for new exams periodically without manual intervention.
- **Smart Tracking:** Uses SQLite to remember which exams have already been broadcasted, preventing duplicate alerts.
- **Docker Ready:** Includes a `Dockerfile` and `docker-compose.yml` for zero-dependency deployment anywhere.

## 🚀 Quick Start (Linux / VM)

If you are on a Linux VM, you can use the provided setup script to handle dependencies and run the bot automatically:

```bash
# 1. Clone and enter the directory
git clone https://github.com/SadeepSachintha/Government-Exam-Tracker.git
cd Government-Exam-Tracker

# 2. Make the script executable
chmod +x run.sh

# 3. Run the bot
./run.sh
```

Once started, you can access the **Web Dashboard** at:
`http://localhost:5000` (or your VM's IP address)

## 💻 Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SadeepSachintha/Government-Exam-Tracker.git
   cd Government-Exam-Tracker
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
   python3 bot.py
   ```

## 🐳 Deployment (Docker / Ubuntu VM)

If you prefer using Docker for a clean, isolated environment:

1. **Configure your `.env` file** as shown above.

2. **Deploy the container:**
   ```bash
   sudo docker-compose up -d --build
   ```

3. **View live logs:**
   ```bash
   sudo docker-compose logs -f
   ```

---
*Built with Python, python-telegram-bot, and Docker.*
