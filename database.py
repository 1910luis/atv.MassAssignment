import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0
        )
    ''')
    cursor.execute("DELETE FROM users")
    cursor.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)", ("admin", "admin123", 1))
    cursor.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)", ("user", "user123", 0))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
