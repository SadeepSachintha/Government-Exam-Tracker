FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DB_FILE=/app/data/bot.db
ENV PORT=5000

WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Ensure run.sh is executable
RUN chmod +x run.sh

# Expose the dashboard port
EXPOSE 5000

# Set a volume for the database to persist data
VOLUME ["/app/data"]

# Run the startup script
CMD ["./run.sh"]

