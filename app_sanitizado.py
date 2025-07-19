from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        is_admin = 0

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)", (username, password, is_admin))
        conn.commit()
        conn.close()

        return f"Usuário {username} registrado com sucesso (sem privilégios)!"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
