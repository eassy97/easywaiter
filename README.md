# Easywaiter Flask App

This repository contains a minimal Flask application with a simple login system.
User credentials are stored in a plain text file `users.txt` in the format `username:password`.

## Setup
1. Install dependencies (Flask):
   ```bash
   pip install flask
   ```
   If you do not have network access, make sure Flask is available in your environment.

2. Run the application:
   ```bash
   python app.py
   ```
   The app will start in debug mode on `http://localhost:5000`.

## Default Credentials
An example user is included:
- **Username:** `admin`
- **Password:** `password`

Add new users by appending lines in the same `username:password` format to `users.txt`.
