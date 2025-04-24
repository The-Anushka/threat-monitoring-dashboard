import json
import random
import time
from datetime import datetime

# Sample data
sources = ["192.168.1.10", "172.16.5.8", "203.0.113.1", "10.1.2.3"]
destinations = ["10.0.0.5", "10.0.0.20", "192.168.0.15"]
threats = ["Port Scan", "SQL Injection", "DDoS", "Malware", "Brute Force"]
severities = ["Low", "Medium", "High"]

while True:
    with open("logs.json", "r") as f:
        logs = json.load(f)

    new_log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_ip": random.choice(sources),
        "destination_ip": random.choice(destinations),
        "threat_type": random.choice(threats),
        "severity": random.choice(severities)
    }

    logs.insert(0, new_log)  # Add to the beginning
    logs = logs[:20]  # Limit to 20 logs max

    with open("logs.json", "w") as f:
        json.dump(logs, f, indent=4)

    print(f"Added new log: {new_log}")
    time.sleep(5)  # Add a new log every 5 seconds
