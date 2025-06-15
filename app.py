"""Main Flask application."""

import os
import sys

try:
    from flask import (
        Flask,
        render_template,
        request,
        redirect,
        url_for,
        session,
    )
    from werkzeug.security import generate_password_hash, check_password_hash
except ModuleNotFoundError as e:  # pragma: no cover - dependency check
    missing = str(e).split("No module named ")[-1].strip("'")
    print(
        f"Missing dependency: {missing}.\n"
        "Install required packages with 'pip install flask werkzeug'.",
        file=sys.stderr,
    )
    raise

app = Flask(__name__)
app.secret_key = 'replace-with-a-secure-random-key'

# Always load the user file relative to this script so it works regardless
# of the current working directory.
USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.txt')

# Helper function to load users from the text file

def load_users():
    """Return a dict of username to hashed password."""
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or ':' not in line:
                    continue
                username, hashed = line.split(':', 1)
                users[username] = hashed
    return users


def verify_credentials(username: str, password: str) -> bool:
    """Check provided credentials against the stored hash."""
    users = load_users()
    hashed = users.get(username)
    if not hashed:
        return False
    return check_password_hash(hashed, password)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if verify_credentials(username, password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Neplatné uživatelské jméno nebo heslo.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

if __name__ == '__main__':
    app.run(debug=True, port=8080)
