import sqlite3

conn = sqlite3.Connection("database.sqlite3")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users (
    user_id integer UNIQUE,
    status integer default 0,
    money integer default 0,
    count_orders integer default 0,
    who_ref integer default 0
);""")

cursor.execute("""CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    who_pays_id integer text,
    what_ordered text,
    order_description text
);""")