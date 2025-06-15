# Easywaiter Flask App

This repository contains a minimal Flask application with a simple login system.
User credentials are stored in a plain text file `users.txt` in the format `username:hashed_password`.

## Setup
1. Install dependencies:
   ```bash
   pip install flask werkzeug
   ```
   If you do not have network access, make sure these packages are available in your environment.

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

Passwords in `users.txt` are hashed using Werkzeug. To add a new user run:
```bash
python - <<'PY'
from werkzeug.security import generate_password_hash
username = 'newuser'
password = 'mypassword'
print(f"{username}:{generate_password_hash(password)}")
PY
```
Append the printed line to `users.txt`.
