import sqlite3

conn = sqlite3.connect('slickdeals.db')
c = conn.cursor()

def check_empty():
    c.execute('SELECT * FROM firedeals')
    return c.fetchone() == None

def insert(str):
    title = (str, )
    c.execute('INSERT INTO firedeals (title) VALUES (?)', title)
    conn.commit()

def find(str):
    title = (str, )
    c.execute('SELECT title FROM firedeals WHERE title LIKE ?', title)
    return not c.fetchone() == None
