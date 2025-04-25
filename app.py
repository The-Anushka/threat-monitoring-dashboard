import random
from datetime import datetime, timedelta
from flask import Flask, jsonify, render_template, request, redirect, url_for, session, send_file, make_response
import sqlite3
import csv
import io

app = Flask(__name__)
app.secret_key = "secret123"  # For sessions

def init_db():
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (timestamp TEXT, source_ip TEXT, destination_ip TEXT, threat_type TEXT, severity TEXT)''')
    conn.commit()
    conn.close()

def generate_fake_logs(n=20):
    severities = ['Low', 'Medium', 'High']
    types = ['Port Scan', 'SQL Injection', 'XSS Attack', 'Brute Force', 'Malware']
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    for _ in range(n):
        timestamp = datetime.now() - timedelta(minutes=random.randint(1, 500))
        source_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
        destination_ip = f"10.0.{random.randint(0, 255)}.{random.randint(0, 255)}"
        threat_type = random.choice(types)
        severity = random.choice(severities)
        c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?)", (timestamp, source_ip, destination_ip, threat_type, severity))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            error = "Wrong credentials"
    return render_template("login.html", error=error)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/api/logs')
def get_logs():
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 50")
    rows = c.fetchall()
    conn.close()

    return jsonify([
        {
            'timestamp': row[0],
            'source_ip': row[1],
            'destination_ip': row[2],
            'threat_type': row[3],
            'severity': row[4]
        }
        for row in rows
    ])

@app.route('/api/export')
def export_logs():
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM logs")
    rows = c.fetchall()
    conn.close()

    # Write CSV to memory using StringIO
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Timestamp", "Source IP", "Destination IP", "Threat Type", "Severity"])
    writer.writerows(rows)

    # Return the CSV as a downloadable file
    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=threat_logs.csv"
    response.headers["Content-type"] = "text/csv"
    return response

if __name__ == '__main__':
    init_db()
    generate_fake_logs()
    app.run(debug=True)



