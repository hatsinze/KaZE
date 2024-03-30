from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Specify the absolute path to the templates directory
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app.template_folder = template_dir

@app.route('/')
def index():
    conn = sqlite3.connect('chatbox.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)''')
    conn.commit()
    conn.close()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    if message:
        conn = sqlite3.connect('chatbox.db')
        c = conn.cursor()
        c.execute("INSERT INTO messages (content) VALUES (?)", (message,))
        conn.commit()
        conn.close()
    return redirect('/')

@app.route('/get_messages')
def get_messages():
    conn = sqlite3.connect('chatbox.db')
    c = conn.cursor()
    c.execute("SELECT * FROM messages ORDER BY id DESC LIMIT 10")
    messages = c.fetchall()
    conn.close()
    return {'messages': messages}

if __name__ == '__main__':
    app.run(debug=True)
