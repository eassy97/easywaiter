# Easywaiter Flask App

This repository contains a minimal Flask application with a simple login system.
User credentials are stored in a plain text file `users.txt` in the format `username:password`.

## Setup
1. Install dependencies:
   ```bash
   pip install flask
   ```
   If you do not have network access, make sure Flask is available in your environment.

2. Run the application:
   ```bash
   python3 app.py
   ```
   Because the app loads `users.txt` relative to its own location,
   you can invoke it from any folder (e.g. `python3 /path/to/app.py`).
   The server will start in debug mode on `http://localhost:8080`.

   A convenience script `start.sh` is also provided if you prefer
   to launch via `./start.sh`.

## Default Credentials
An example user is included:
- **Username:** `admin`
- **Password:** `password`
To add a new user simply append a line in the format `username:password`
to `users.txt`.
