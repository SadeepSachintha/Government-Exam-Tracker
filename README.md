# 🎓 SL Government Exam Tracker Bot

A lightweight, automated Telegram Bot that monitors the [Department of Examinations Sri Lanka](https://applications.doenets.lk/exams) website and instantly notifies subscribers when new government exams are posted.

[![Live Demo](https://img.shields.io/badge/Live-Demo-d4af37?style=for-the-badge&logo=github)](https://SadeepSachintha.github.io/Government-Exam-Tracker/)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

---

## ✨ Features

-   **🚀 Real-time Notifications:** Get alerts directly on your phone as soon as an exam is published.
-   **💎 Premium Web Dashboard:** A beautiful, dark-mode web interface to monitor subscribers, tracked exams, and bot health.
-   **🤖 Interactive Commands:** Users can easily opt-in, check their status, or request immediate updates using commands like `/start`, `/status`, and `/latest`.
-   **🕒 Automated Polling:** Background jobs check for new exams periodically.
-   **💾 Smart Tracking:** Uses SQLite to ensure no duplicate alerts are ever sent.
-   **🐳 Docker Ready:** One-command deployment using Docker and Docker Compose.
-   **☁️ Railway Optimized:** Pre-configured for easy deployment on Railway with persistent storage.

---

## 🤖 Bot Commands

| Command | Description |
| :--- | :--- |
| `/start` | Subscribe to receive notifications for new exams. |
| `/stop` | Unsubscribe from the notification service. |
| `/help` | Show all available commands. |
| `/status`| Check your subscription status. |
| `/latest`| Fetch the currently ongoing exams immediately. |

---

## ☁️ Deployment on Railway

This project is optimized for [Railway](https://railway.app/). To deploy:

1.  **Connect your Repo**: Create a new project on Railway and link this GitHub repository.
2.  **Environment Variables**: Add the following in the **Variables** tab:
    -   `TELEGRAM_BOT_TOKEN`: Your token from @BotFather.
    -   `DB_FILE`: Set to `/app/data/bot.db` for persistent storage.
    -   `POLL_INTERVAL`: (Optional) Seconds between checks (default: `86400`).
3.  **Setup Volume**: 
    -   Go to **Settings** -> **Volumes**.
    -   Create a Volume and mount it to `/app/data`. This ensures your subscriber data isn't lost during deployments.
4.  **Networking**: Railway will automatically detect the Flask dashboard on port 5000. Generate a domain in **Settings** -> **Networking** to access it.

---

## 🐳 Local Deployment (Docker)

```bash
# 1. Configure .env file with your TELEGRAM_BOT_TOKEN
# 2. Build and start the containers
docker compose up -d --build

# 3. View logs
docker compose logs -f
```

---

## 🛠️ Local Development (Manual)

```bash
# 1. Clone the repository
git clone https://github.com/SadeepSachintha/Government-Exam-Tracker.git
cd Government-Exam-Tracker

# 2. Setup Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Run both Bot and Dashboard
chmod +x run.sh
./run.sh
```

---

## 🛠️ Configuration (.env)

| Variable | Description | Default |
| :--- | :--- | :--- |
| `TELEGRAM_BOT_TOKEN` | Your Telegram Bot Token from @BotFather | (Required) |
| `POLL_INTERVAL` | Interval in seconds to check for new exams | `86400` (24h) |
| `DB_FILE` | Path to the SQLite database file | `bot.db` |
| `PORT` | Port for the web dashboard | `5000` |

---

## 🔍 Troubleshooting

#### `telegram.error.Conflict`
This means the same bot token is running elsewhere. 
- **Solution**: Regenerate your token via @BotFather and update your `.env` file or Railway variables.

#### `Port 5000 is already in use`
The dashboard is already running.
- **Solution**: On Linux, run `pkill -f dashboard.py`. On Railway, this is handled automatically.

---

### 👨‍💻 Developed by **Sadeep Sachintha**
*All rights reserved &copy; 2026*

*Built with Python, Flask, and ❤️ for students in Sri Lanka.*
