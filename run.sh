#!/bin/bash

# Ensure we are in the app directory
cd "$(dirname "$0")"

# Create data directory if it doesn't exist
mkdir -p data

# Start the dashboard in the background
echo "Starting Dashboard..."
python dashboard.py &

# Start the bot in the foreground
echo "Starting the bot..."
python bot.py
