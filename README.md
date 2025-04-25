🚀 Project Overview
Threat Watch Dashboard is a real-time web-based cybersecurity tool built using Flask and SQLite, designed to simulate threat detection and monitoring systems like those used in Security Operations Centers (SOCs). The app dynamically generates fake log entries, displays threats visually, and allows analysts (users) to filter, export, and investigate suspicious activity — all from a sleek and responsive dashboard.

🎯 Key Objectives
Simulate threat log monitoring in a realistic environment

Visualize network threat patterns and severity

Enable basic security analysis using modern UI tools

Offer a secure login system for controlled access

Deploy the dashboard publicly for easy showcase and use

🛠️ Tech Stack

Layer	Technology Used
Backend	Python (Flask)
Database	SQLite
Frontend	HTML, CSS, JavaScript
Charts	Chart.js
Deployment	Render.com
Export Format	CSV
Auth Layer	Flask Sessions
🔧 Features & Functionality
✅ 1. Log Generation
Generates fake cybersecurity threat logs (e.g. SQL Injection, Port Scans, etc.)

Includes metadata like timestamp, IP addresses, threat type, and severity

Stored in a persistent SQLite database

✅ 2. Dashboard with Filtering
Displays threat logs with colored indicators based on severity (High/Medium/Low)

Allows real-time filtering by severity

✅ 3. Visual Analytics
Uses Chart.js to generate bar charts of threat type frequency

Helps users spot patterns in attack types

✅ 4. Export Logs
Download logs as a CSV file for offline analysis or archiving

Handles edge cases cleanly (e.g., if no logs present)

✅ 5. Authentication
Users must login to access the dashboard (admin / password)

Credentials are customizable

Login page is styled with modern UI for public presentation

✅ 6. Deployment
Live and accessible on Render at:
🌐 https://threat-watch-dashboard.onrender.com

🔐 Security Concepts Simulated
Log Analysis

Threat Classification

Access Control

Attack Vectors: SQL Injection, XSS, Brute Force, Port Scans, Malware
