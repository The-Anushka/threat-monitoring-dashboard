# db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('threat_logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source_ip TEXT,
            destination_ip TEXT,
            threat_type TEXT,
            severity TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_log(timestamp, source_ip, destination_ip, threat_type, severity):
    conn = sqlite3.connect('threat_logs.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO logs (timestamp, source_ip, destination_ip, threat_type, severity)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, source_ip, destination_ip, threat_type, severity))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect('threat_logs.db')
    c = conn.cursor()
    c.execute('SELECT timestamp, source_ip, destination_ip, threat_type, severity FROM logs ORDER BY timestamp DESC LIMIT 50')
    logs = c.fetchall()
    conn.close()
    return logs
