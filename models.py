import sqlite3 as sql

def loginUser(username, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    # SQL injection zaifligi
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("[DEBUG] SQL query:", query)
    cur.execute(query)
    result = cur.fetchone()
    con.close()
    return result is not None

def createUsersTable():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    con.commit()
    con.close()
