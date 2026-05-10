import os
import sqlite3
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
DB_FILE = os.getenv("DB_FILE", "bot.db")

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    conn = get_db_connection()
    try:
        subscribers = conn.execute('SELECT COUNT(*) FROM subscribers').fetchone()[0]
        exams = conn.execute('SELECT COUNT(*) FROM tracked_exams').fetchone()[0]
        recent_exams = conn.execute('SELECT name, added_at FROM tracked_exams ORDER BY added_at DESC LIMIT 5').fetchall()
        
        return jsonify({
            'subscribers': subscribers,
            'total_exams': exams,
            'recent_exams': [dict(row) for row in recent_exams]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
