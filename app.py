from flask import Flask, render_template_string, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'replace-with-a-secure-random-key'

USERS_FILE = 'users.txt'

# Helper function to load users from the text file

def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ':' not in line:
                    continue
                username, password = line.split(':', 1)
                users[username] = password
    return users

@app.route('/')
def index():
    if 'username' in session:
        return render_template_string('''
            <h1>Vítejte {{username}}!</h1>
            <a href="{{ url_for('logout') }}">Odhlásit</a>
        ''', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        users = load_users()
        if users.get(username) == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Neplatné uživatelské jméno nebo heslo.'
    return render_template_string('''
        <h2>Přihlášení</h2>
        {% if error %}<p style="color:red;">{{error}}</p>{% endif %}
        <form method="post">
            <label>Uživatel:</label>
            <input type="text" name="username" required><br>
            <label>Heslo:</label>
            <input type="password" name="password" required><br>
            <input type="submit" value="Přihlásit">
        </form>
    ''', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
