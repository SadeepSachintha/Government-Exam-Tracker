FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set a volume for the database to persist data
VOLUME ["/app/data"]

# Overwrite DB_FILE to point to the volume
ENV DB_FILE=/app/data/bot.db

# Run the bot
CMD ["python", "bot.py"]
