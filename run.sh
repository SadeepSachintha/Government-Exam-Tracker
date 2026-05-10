#!/bin/bash

# Ensure we are in the app directory
cd "$(dirname "$0")"

# Create data directory if it doesn't exist (for SQLite persistence)
mkdir -p data

# Check if we are running in a container or locally
if [ -f "venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
elif [ -d "venv" ]; then
    echo "Venv exists but activate script not found. Skipping activation."
else
    echo "No virtual environment found. Running with system python (typical for Docker)."
fi

# Start the dashboard in the background
echo "Starting Dashboard..."
python3 dashboard.py &

# Start the bot in the foreground
echo "Starting the bot..."
python3 bot.py

