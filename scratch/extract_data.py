import sqlite3
import json
import os

DB_FILE = "bot.db"

def extract():
    if not os.path.exists(DB_FILE):
        print(json.dumps({"subscribers": 0, "total_exams": 0, "recent_exams": []}))
        return

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    subscribers = cursor.execute('SELECT COUNT(*) FROM subscribers').fetchone()[0]
    exams = cursor.execute('SELECT COUNT(*) FROM tracked_exams').fetchone()[0]
    recent_exams = cursor.execute('SELECT name, added_at FROM tracked_exams ORDER BY added_at DESC LIMIT 10').fetchall()
    
    data = {
        'subscribers': subscribers,
        'total_exams': exams,
        'recent_exams': [dict(row) for row in recent_exams]
    }
    
    print(json.dumps(data, indent=2))
    conn.close()

if __name__ == "__main__":
    extract()
