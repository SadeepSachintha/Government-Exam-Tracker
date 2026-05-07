# 🎓 SL Government Exam Tracker Bot

A lightweight, automated Telegram Bot that monitors the [Department of Examinations Sri Lanka](https://applications.doenets.lk/exams) website and instantly notifies subscribers when new government exams are posted.

[![Live Demo](https://img.shields.io/badge/Live-Demo-d4af37?style=for-the-badge&logo=github)](https://SadeepSachintha.github.io/Government-Exam-Tracker/)

---

## ✨ Features

-   **🚀 Real-time Notifications:** Get alerts directly on your phone as soon as an exam is published.
-   **💎 Premium Web Dashboard:** A beautiful, dark-mode web interface to monitor subscribers, tracked exams, and bot health.
-   **📈 Static Demo:** A hosted version of the dashboard available on GitHub Pages for quick previewing.
-   **🤖 Easy Subscriptions:** Users can easily opt-in or opt-out by messaging `/start` and `/stop`.
-   **🕒 Automated Polling:** Background jobs check for new exams periodically.
-   **💾 Smart Tracking:** Uses SQLite to ensure no duplicate alerts are ever sent.
-   **🐳 Docker Ready:** One-command deployment using Docker and Docker Compose.

---

## 🌐 Live Demo Dashboard

Check out the interactive demo hosted on GitHub Pages:
👉 **[SadeepSachintha.github.io/Government-Exam-Tracker/](https://SadeepSachintha.github.io/Government-Exam-Tracker/)**

> [!NOTE]
> The demo is a static snapshot of the system. For full live tracking functionality, deploy the bot using the instructions below.

---

## 🚀 Quick Start (Linux / VM)

If you are on a Linux VM, use the provided setup script to handle dependencies and run everything automatically:

```bash
# 1. Clone the repository
git clone https://github.com/SadeepSachintha/Government-Exam-Tracker.git
cd Government-Exam-Tracker

# 2. Configure your environment
# Create a .env file and add your TELEGRAM_BOT_TOKEN

# 3. Make the script executable
chmod +x run.sh

# 4. Run the bot & dashboard
./run.sh
```

> [!TIP]
> Once started, access your **Live Web Dashboard** at `http://your-vm-ip:5000`

---

## 🤖 Bot Commands

| Command | Description |
| :--- | :--- |
| `/start` | Subscribe to receive notifications for new exams. |
| `/stop` | Unsubscribe from the notification service. |

---

## 🛠️ Configuration (.env)

| Variable | Description | Default |
| :--- | :--- | :--- |
| `TELEGRAM_BOT_TOKEN` | Your Telegram Bot Token from @BotFather | (Required) |
| `POLL_INTERVAL` | Interval in seconds to check for new exams | `86400` (24h) |
| `DB_FILE` | Path to the SQLite database file | `bot.db` |

---

## 🐳 Deployment with Docker

```bash
# 1. Build and start the containers
docker compose up -d --build

# 2. View logs
docker compose logs -f
```

---

## 🔍 Troubleshooting

#### `telegram.error.Conflict`
This means the same bot token is running elsewhere. 
- **Solution**: Regenerate your token via @BotFather and update your `.env` file.

#### `Port 5000 is already in use`
The dashboard is already running in the background.
- **Solution**: Run `pkill -f dashboard.py` and restart `./run.sh`.

---

### 👨‍💻 Developed by **Sadeep Sachintha**
*All rights reserved &copy; 2026*

*Built with Python, Flask, and ❤️ for students in Sri Lanka.*
