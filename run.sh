#!/bin/bash
cd "$(dirname "$0")"

# Trap SIGINT and SIGTERM to kill background processes when the script exits
trap "kill 0" EXIT

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Start the dashboard in the background
echo "Starting Dashboard on http://localhost:5000 ..."
python3 dashboard.py &

# Run the bot
echo "Starting the bot..."
python3 bot.py
