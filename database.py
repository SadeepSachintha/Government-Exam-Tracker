import sqlite3
import os

DB_FILE = os.getenv("DB_FILE", "bot.db")

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    # Table for subscribers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            chat_id INTEGER PRIMARY KEY,
            subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Table for tracked exams to avoid duplicate notifications
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tracked_exams (
            exam_id TEXT PRIMARY KEY,
            name TEXT,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_subscriber(chat_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subscribers (chat_id) VALUES (?)", (chat_id,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False # Already subscribed
    finally:
        conn.close()

def remove_subscriber(chat_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subscribers WHERE chat_id = ?", (chat_id,))
    conn.commit()
    conn.close()

def get_subscribers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT chat_id FROM subscribers")
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return users

def is_exam_new(exam_id, name):
    """
    Checks if an exam is new. If new, it adds to DB and returns True.
    If it already exists, returns False.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT exam_id FROM tracked_exams WHERE exam_id = ?", (exam_id,))
    exists = cursor.fetchone()
    
    if not exists:
        cursor.execute("INSERT INTO tracked_exams (exam_id, name) VALUES (?, ?)", (exam_id, name))
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False
