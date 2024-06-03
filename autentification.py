from flask import Flask, request, jsonify, render_template, url_for, redirect
import sqlite3
import hashlib

app = Flask(__name__)

# Создаем базу данных SQLite
conn = sqlite3.connect('databases/users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
conn.commit()
conn.close()


# Регистрация пользователя
@app.route('/register/', methods=['POST', 'get'])
def register():
    if request.method == 'POST':
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')

        conn = sqlite3.connect('databases/users.db')
        c = conn.cursor()
        # Хэшируем пароль перед сохранением в базу данных
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute("SELECT * FROM users WHERE username=?", username)
        user = c.fetchone()
        if user:
            message = "The user with the same name exists. Try to come up with another name."
            return render_template('login.html', message=message)
        else:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
    else:
        return render_template('register.html', message='Registration')


# Авторизация пользователя
@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')

        conn = sqlite3.connect('databases/users.db')
        c = conn.cursor()
        # Хэшируем введенный пароль для сравнения с паролем из базы данных
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = c.fetchone()
        conn.close()
        if user:
            return redirect(url_for('admin'))
            # return render_template('admin.html', message=message)
        else:
            message = "Wrong username or password"
            return render_template('login.html', message=message)
    else:
        return render_template('login.html', message='Log in')


@app.route('/admin/', methods=['GET'])
def admin():
    message = "Correct username and password"
    return render_template('admin.html', message='good')


if __name__ == '__main__':
    app.run(debug=True)
