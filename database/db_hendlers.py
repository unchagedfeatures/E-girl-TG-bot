import sqlite3
db_path = r'database\database.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
conn.commit()
#cursor.execute("PRAGMA journal_mode = WAL")
#cursor.execute("PRAGMA wal_autocheckpoint = 1")

def get_user(cursor, user_id):
    return cursor.execute("SELECT * FROM users WHERE user_id=?;", (user_id, )).fetchone()


def add_user(conn, cursor, user_id, city):
    try:
        cursor.execute("INSERT INTO users (user_id, city) VALUES (?, ?);", (user_id, city, ))
        conn.commit()
        return True
    except:
        return False

def change_status(conn, cursor, user_id):
    try:
        cursor.execute("UPDATE users SET status=? WHERE user_id=?;", (1, user_id, ))
        conn.commit()
        cursor.execute("INSERT INTO workers (worker_id) VALUES (?);", (user_id, ))
        conn.commit()
        return True
    except:
        return False

def get_worker(cursor, user_id):
    return cursor.execute("SELECT * FROM users WHERE user_id=? AND status=?;", (user_id, 1, )).fetchone()

def get_admin(cursor, user_id):
    return cursor.execute("SELECT * FROM users WHERE user_id=? AND status=?;", (user_id, 2, )).fetchone()

def get_balance(cursor, user_id):
    return cursor.execute("SELECT money FROM users WHERE user_id = ?", (user_id,)).fetchone()